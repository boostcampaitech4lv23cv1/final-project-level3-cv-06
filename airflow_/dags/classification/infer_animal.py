import os
import sys
from glob import glob

import albumentations as A
import cv2
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.feather as feather
import requests
import timm
import torch
import yaml
from albumentations.core.composition import Compose
from albumentations.pytorch import ToTensorV2
from PaintTransformer.inference import inference, init
from PIL import Image
from pytorch_lightning import LightningModule, Trainer
from sqlalchemy import create_engine
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm

AIRFLOW_HOME = os.path.dirname(os.path.abspath(__file__))


KEYWORD, SITE, SCRAPED_TIME = sys.argv[1:]
# KEYWORD, SITE, SCRAPED_TIME = "animal", "pixabay", "02-03_22"
with open(
    f"{os.path.abspath(os.path.join(AIRFLOW_HOME, '..','..'))}/secret.yml", "r"
) as f:
    secret = yaml.load(f, Loader=yaml.FullLoader)


class ClassifyDataset(Dataset):
    def __init__(self, df, transform=None):
        base_path = f"{AIRFLOW_HOME}/data/"
        self.img_tag = df["tag"]
        self.img_path = base_path + df["img_path"]
        self.transform = transform

    def __len__(self):
        return len(self.img_path)

    def __getitem__(self, idx):
        img_path = self.img_path[idx]
        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if self.transform:
            image = self.transform(image=image)

        image_tag = self.img_tag[idx]
        return image["image"], image_tag


class Model(LightningModule):
    def __init__(self):
        super().__init__()
        self.model = timm.create_model(
            model_name="eva_giant_patch14_336.m30m_ft_in22k_in1k", pretrained=True
        )

    def forward(self, x):
        return self.model(x)

    def predict_step(self, batch, batch_idx):
        imgs, img_tags = batch
        logits = self.model(imgs)
        preds = logits.argmax(dim=1)
        return preds


def read_feather(file_path):
    if os.path.isfile(file_path):
        return pd.read_csv(file_path)
    else:
        assert os.path.isfile(file_path), f"{file_path} is not found"


def get_metadata_from_api() -> pd.DataFrame:
    """get metadata from api

    Returns:
        pd.DataFrame: metadata dataframe
    """
    url = f"{secret['api_url']}/api/v1/meta/read?category=animal"
    res = requests.get(url, allow_redirects=False)
    df = res.json()
    df = pd.DataFrame(df)
    return df


def inference_img(df: pd.DataFrame) -> np.ndarray:
    """inference from crawled images using imagenet pretrained model

    Args:
        df (pd.DataFrame): crawled images metadata

    Returns:
        np.ndarray: prediction from model (imgnet class)
    """
    transform = Compose([A.Resize(height=336, width=336), A.Normalize(), ToTensorV2()])
    test_set = ClassifyDataset(df, transform)
    test_loader = DataLoader(
        test_set, batch_size=set_batch_size(test_set, 4), shuffle=False, num_workers=4
    )
    model = Model()
    trainer = Trainer(accelerator="gpu", logger=False)
    predictions = trainer.predict(model, test_loader)
    predictions = torch.concat(predictions).cpu().detach().numpy()

    return predictions


def set_batch_size(data_set, batch_size):
    return min(batch_size, len(data_set))


def pred2imgnetlabel(predictions: np.array, imagenet_labels: pd.DataFrame) -> list:
    """prediction to imagenet label

    remove label that is not for usage
    ("use" column value is 0)

    Args:
        predictions (np.array): prediction from model (imgnet class)
        imagenet_labels (pd.DataFrame): imagenet korean labels

    Returns:
        list: korean labels that match with prediction
    """
    df = imagenet_labels.loc[predictions]
    for i in df[df["use"] == 0].index:
        df.loc[i, "korean"] = "NaN"
    df["use"] = df["use"].astype("bool")
    return list(df["korean"]), list(df["use"])


def read_imgnet_labels() -> pd.DataFrame:
    """read imagenet labels

    Returns:
        pd.DataFrame: imagenet label dataframe
    """
    df = pd.read_csv(f"{AIRFLOW_HOME}/imagenet_class.csv")
    df.drop("english", axis=1, inplace=True)
    return df


def make_img_label() -> pd.DataFrame:
    """make a label from crawled images
    1. read labels
    2. inference from crawled images using imagenet pretrained model
    3. convert prediction to label

    Returns:
        Dataframe: df + crawled imgs prediction labels
    """

    imagenet_labels = read_imgnet_labels()
    df = get_metadata_from_api()
    predictions = inference_img(df)
    labels, uses = pred2imgnetlabel(predictions, imagenet_labels)
    df["label"] = labels
    df["use_status"] = uses
    print(
        f"The number use_status(True) is {df['use_status'].value_counts()[True]}/{len(uses)}!"
    )

    return df


def join_df2db(df: pd.DataFrame, host: str = "34.145.38.251"):
    """join prediction labels to table in gcp docker container PostgreSQL
    1. read table from PostgreSQL
    2. merge prediction labels to table
    3. update table in PostgreSQL

    Args:
        df (pd.DataFrame): dataframe with prediction labels
        host (str): host address of gcp docker container PostgreSQL
    """
    # PostgreSQL configs
    user = "airflow"
    password = "airflow"
    port = 5432
    database = "airflow"

    # connect to PostgreSQL
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

    # Read the table from PostgreSQL
    new_df = pd.read_sql_table(KEYWORD, engine)
    new_df["label"] = new_df["label"].fillna("")

    # merge prediction labels to table
    new_df = pd.merge(new_df, df, on="img_path", how="left", suffixes=("", "_y"))
    new_df["label_y"] = new_df["label_y"].fillna("")
    new_df["label"] = new_df["label"] + new_df["label_y"]
    new_df = new_df.filter(regex="^(?!.*_y$).*")

    # Update the table in PostgreSQL
    new_df.to_sql(name=KEYWORD, con=engine, if_exists="replace", index=False)


def send_metadata2api(df: pd.DataFrame, KEYWORD: str) -> None:
    """send metadata dataframe to api server

    Args:
        df (pd.DataFrame): metadata dataframe
        KEYWORD (str): keyword for metadata
    """
    df = df.drop("tag", axis=1)
    url = f"{secret['api_url']}/api/v1/meta/update"

    buffer = pa.BufferOutputStream()
    feather.write_feather(df, buffer)

    file = {"file": buffer.getvalue().to_pybytes()}
    category = {"category": KEYWORD}
    res = requests.post(url, files=file, data=category)

    # Check the status code of the response
    try:
        res.raise_for_status()
    except Exception as e:
        print(e)


def make_duration_list(
    num_frame: int = 200, total_time: int = 10, mode: str = "LINEAR"
) -> list:
    """make frame duration list for animation

    Args:
        num_frame (int, optional): number of frames. Defaults to 200.
        total_time (int, optional): total time of animation. Defaults to 10.
        mode (str, optional): mode of duration list. Defaults to "LINEAR".

    Returns:
        list: duration list
    """

    exp_dict = {
        "SQRT": 0.5,
        "LINEAR": 1,
        "SQUARE": 2,
    }
    min_time_step = 12

    if mode == "CONSTANT":
        return [round(total_time * 1000 / num_frame)] * num_frame
    else:
        exp_num = exp_dict[mode]
        duration_list = np.arange(min_time_step, min_time_step + num_frame)
        duration_list = np.power(duration_list, exp_num)
        duration_list = np.asarray(
            duration_list / sum(duration_list) * total_time * 1000, dtype=int
        )
        duration_list[duration_list < min_time_step] = min_time_step
        return list(duration_list)


def img2ani(df: pd.DataFrame) -> None:
    """convert img to animation

    1. check if img use_status is True
    2. convert img to animation using PaintTransformer
    3. save animation in webp format

    Args:
        df (pd.DataFrame): metadata dataframe
    """

    base_path = f"{AIRFLOW_HOME}/data/"
    time_consume = make_duration_list(num_frame=200, total_time=10, mode="LINEAR")

    resize_l = 1024
    K = 5
    stroke_num = 8
    patch_size = 32

    model, meta_brushes, device = init()

    img_paths = base_path + df["img_path"]

    for img_path, use_status in tqdm(zip(img_paths, df["use_status"])):
        if use_status:
            save_path = img_path.split(".")[0] + "_ani.webp"
            image = Image.open(img_path)
            output = inference(
                image=image,
                resize_l=resize_l,  # resize original input to this size. (max(w, h) = resize_l)
                K=K,  # set K
                device=device,
                model=model,
                meta_brushes=meta_brushes,
                stroke_num=stroke_num,
                patch_size=patch_size,
            )
            Image.Image.save(
                output[0],
                save_path,
                format="WEBP",
                save_all=True,
                append_images=output[1:],
                optimize=True,
                duration=time_consume,
                loop=1,
            )


if __name__ == "__main__":

    df = make_img_label()
    send_metadata2api(df)
    img2ani(df)
    print("label: ", df["label"])
# TODO animation 인메모리로 GCS 전송
