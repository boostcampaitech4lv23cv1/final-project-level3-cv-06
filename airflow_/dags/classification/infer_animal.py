import os
import sys
from glob import glob

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

AIRFLOW_HOME = "/opt/ml/final-project-level3-cv-06/airflow_"

KEYWORD, SITE, SCRAPED_TIME = sys.argv[1:]
# KEYWORD, SITE, SCRAPED_TIME = "animals", "pixabay", "01-27_11"


class ClassifyDataset(Dataset):
    def __init__(self, df, transform=None):
        base_path = f"{AIRFLOW_HOME}/dags/classification/data"
        path = os.path.join(base_path, KEYWORD, SITE, SCRAPED_TIME, "*.jpg")
        self.img_tag = df["tag"]
        self.img_path = glob(path)
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
        return pd.read_feather(file_path)
    else:
        assert os.path.isfile(file_path), f"{file_path} is not found"


def inference(df) -> np.ndarray:
    transform = Compose([A.Resize(height=224, width=224), A.Normalize(), ToTensorV2()])
    test_set = ClassifyDataset(df, transform)
    test_loader = DataLoader(test_set, batch_size=1, shuffle=False, num_workers=4)
    model = Model()
    trainer = Trainer(accelerator="gpu")
    predictions = trainer.predict(model, test_loader)
    predictions = torch.concat(predictions).cpu().detach().numpy()

    return predictions


def pred2imgnetlabel(predictions, imagenet_labels):

    return imagenet_labels[predictions]


def read_imgnet_labels():
    with open(f"{AIRFLOW_HOME}/dags/classification/imagenet_class.yaml", "r") as f:
        labels = yaml.load(f, Loader=yaml.FullLoader)
        return np.array(labels)


def make_img_label() -> pd.DataFrame:
    """make a label from crawled images
    1. read labels
    2. inference from crawled images using imagenet pretrained model
    3. convert prediction to label

    Returns:
        Dataframe: df + crawled imgs prediction labels
    """

    imagenet_labels = read_imgnet_labels()
    base_path = f"{AIRFLOW_HOME}/dags/classification/data"

    df = read_feather(
        os.path.join(base_path, KEYWORD, SITE, SCRAPED_TIME, "metadata.feather")
    )
    predictions = inference(df)
    labels = pred2imgnetlabel(predictions, imagenet_labels)
    df["label"] = labels
    return df


def join_df2db(df):
    user = "airflow"
    password = "airflow"
    host = "34.82.38.106"
    port = 5432
    database = "airflow"

    engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

    new_df = pd.read_sql_table(KEYWORD, engine)
    new_df["label"] = new_df["label"].fillna("")
    # Join the DataFrame with another DataFrame or series
    new_df = pd.merge(new_df, df, on="img_path")
    new_df["label"] = new_df["label_x"] + new_df["label_y"]
    new_df = new_df.drop(columns=["label_x", "label_y"])

    # Update the table in PostgreSQL
    new_df.to_sql(name=KEYWORD, con=engine, if_exists="replace", index=False)


if __name__ == "__main__":

    df = make_img_label()
    print("label: ", df["label"])
    join_df2db(df)

# TODO imgnet 레이블 정리 및 간소화
