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
from pytorch_lightning import LightningModule, Trainer
from sqlalchemy import create_engine
from torch.utils.data import DataLoader, Dataset

AIRFLOW_HOME = os.path.dirname(os.path.abspath(__file__))


KEYWORD, SITE, SCRAPED_TIME = sys.argv[1:]
# KEYWORD, SITE, SCRAPED_TIME = "animal", "pixabay", "02-02_19"


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
        self.model = timm.create_model(model_name="resnet50", pretrained=True)

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
    url = "http://34.64.169.197/api/v1/meta/read"
    res = requests.get(url, allow_redirects=False)
    df = res.json()
    df = pd.DataFrame(df)
    return df


def inference(df) -> np.ndarray:
    transform = Compose([A.Resize(height=224, width=224), A.Normalize(), ToTensorV2()])
    test_set = ClassifyDataset(df, transform)
    test_loader = DataLoader(test_set, batch_size=1, shuffle=False, num_workers=4)
    model = Model()
    trainer = Trainer(accelerator="gpu")
    predictions = trainer.predict(model, test_loader)
    predictions = torch.concat(predictions).cpu().detach().numpy()

    return predictions


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


def read_imgnet_labels():
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
    predictions = inference(df)
    labels, uses = pred2imgnetlabel(predictions, imagenet_labels)
    df["label"] = labels
    df["use_status"] = uses

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


def send_metadata2api(df):
    df = df.drop("tag", axis=1)
    url = "http://34.64.169.197/api/v1/meta/update"

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


if __name__ == "__main__":

    df = make_img_label()
    send_metadata2api(df)
    print("label: ", df["label"])

# TODO imgnet 레이블 정리 및 간소화
