import os

import albumentations as A
import cv2
import numpy as np
import pandas as pd
import timm
import yaml
from albumentations.core.composition import Compose
from albumentations.pytorch import ToTensorV2
from pytorch_lightning import LightningModule, Trainer
from torch.utils.data import DataLoader, Dataset


class ClassifyDataset(Dataset):
    def __init__(self, df, transform=None):
        self.img_path = df["img_path"].values
        self.img_alt = df["img_alt"].values
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


def make_img_label():
    predictions = inference(keyword="dog")

    imagenet_labels = read_labels()
    label = pred2imgnetlabel(predictions, imagenet_labels)

    return label


def inference(keyword="dog"):

    transform = Compose([A.Resize(height=224, width=224), A.Normalize(), ToTensorV2()])
    # test_df = read_feather(path=f"dags/crawled_img/metadata/{keyword}.feather")
    test_df = read_feather(
        f"/Users/juheon/Desktop/jh/final-project-level3-cv-06/airflow_/dags/crawled_img/pixabay/metadata/{keyword}.feather"
    )
    test_set = ClassifyDataset(test_df, transform)
    test_loader = DataLoader(test_set, batch_size=32, shuffle=False, num_workers=4)
    model = Model()
    trainer = Trainer(accelerator="mps")
    predictions = trainer.predict(model, test_loader).concat().cpu().detach().numpy()

    return predictions


def pred2imgnetlabel(predictions, imagenet_labels):

    return imagenet_labels[predictions]


def read_labels():
    # with open("dags/classification/imagenet_class.yaml", "r") as f:
    with open(
        "/Users/juheon/Desktop/jh/final-project-level3-cv-06/airflow_/dags/classification/imagenet_class.yaml",
        "r",
    ) as f:
        labels = yaml.load(f, Loader=yaml.FullLoader)
        return np.array(labels)


if __name__ == "__main__":
    label = make_img_label()
    print("label: ", label)

# TODO airflow 연결, DB 연결
# TODO 이미지 경로 airflow_home에 맞게 변경
# TODO 제작된 label을 간소화해서 DB에 저장