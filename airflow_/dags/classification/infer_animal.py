import os

import albumentations as A
import cv2
import numpy as np
import pandas as pd
import timm
import torch
import yaml
from albumentations.core.composition import Compose
from albumentations.pytorch import ToTensorV2
from pytorch_lightning import LightningModule, Trainer
from sqlalchemy import create_engine
from torch.utils.data import DataLoader, Dataset

AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME")


class ClassifyDataset(Dataset):
    def __init__(self, df, transform=None):
        self.img_path = df["img_path"].values
        self.img_alt = df["alt"].values
        self.transform = transform

    def __len__(self):
        return len(self.img_path)

    def __getitem__(self, idx):
        img_path = self.img_path[idx]
        label = self.img_alt[idx]
        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if self.transform:
            image = self.transform(image=image)
        return image["image"], label


class Model(LightningModule):
    def __init__(self):
        super().__init__()
        self.model = timm.create_model(model_name="resnet50", pretrained=True)

    def forward(self, x):
        return self.model(x)

    def predict_step(self, batch, batch_idx):
        imgs, img_alts = batch
        logits = self.model(imgs)
        preds = logits.argmax(dim=1)
        return preds


def read_feather(file_path):
    if os.path.isfile(file_path):
        return pd.read_feather(file_path)
    else:
        assert os.path.isfile(file_path), f"{file_path} is not found"


def inference(df, feather_name="animal"):
    transform = Compose([A.Resize(height=224, width=224), A.Normalize(), ToTensorV2()])
    test_set = ClassifyDataset(df, transform)
    test_loader = DataLoader(test_set, batch_size=32, shuffle=False, num_workers=4)
    model = Model()
    trainer = Trainer(accelerator="mps")
    predictions = (
        torch.concat(trainer.predict(model, test_loader)).cpu().detach().numpy()
    )

    return predictions


def pred2imgnetlabel(predictions, imagenet_labels):

    return imagenet_labels[predictions]


def read_imgnet_labels():
    with open(f"{AIRFLOW_HOME}/dags/classification/imagenet_class.yaml", "r") as f:
        labels = yaml.load(f, Loader=yaml.FullLoader)
        return np.array(labels)


def make_img_label(feather_name: str) -> pd.DataFrame:
    """make a label from crawled images
    1. read labels
    2. read feather file
    3. inference from crawled images using imagenet pretrained model
    4. convert prediction to label

    Args:
        feather_name (str): name of feather file

    Returns:
        Dataframe: df + crawled imgs prediction labels
    """

    imagenet_labels = read_imgnet_labels()
    df = read_feather(
        f"{AIRFLOW_HOME}/dags/crawled_img/pixabay/metadata/{feather_name}.feather"
    )

    predictions = inference(df, feather_name)
    labels = pred2imgnetlabel(predictions, imagenet_labels)
    df["label"] = labels
    return df[["srcset", "label"]]


def join_df2db(df):
    user = "myuser"
    password = "mypassword"
    host = "localhost"
    port = 5432
    database = "airflow_db"
    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

    animal_df = pd.read_sql_table("animal", engine)
    animal_df["label"] = animal_df["label"].fillna("")
    # Join the DataFrame with another DataFrame or series
    animal_df = pd.merge(animal_df, df, on="srcset")
    animal_df["label"] = animal_df["label_x"] + animal_df["label_y"]
    animal_df = animal_df.drop(columns=["label_x", "label_y"])

    # Update the table in PostgreSQL
    animal_df.to_sql(name="animal", con=engine, if_exists="replace", index=False)
def infer_senddb():
    df = make_img_label(feather_name="animal")
    print("label: ", df["label"])
    join_df2db(df)

if __name__ == "__main__":
    df = make_img_label(feather_name="animal")
    print("label: ", df["label"])
    join_df2db(df)
