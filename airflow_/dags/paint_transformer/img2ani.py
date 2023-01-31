import os
import sys

import pandas as pd
from PaintTransformer.inference import inference, init
from PIL import Image
from tqdm import tqdm

AIRFLOW_HOME = os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
)

# KEYWORD, SITE, SCRAPED_TIME = sys.argv[1:]
KEYWORD, SITE, SCRAPED_TIME = "animal", "pixabay", "01-31_16"


def img2ani():

    base_path = f"{AIRFLOW_HOME}/dags/classification/data/"
    file_path = os.path.join(
        base_path, KEYWORD, SITE, SCRAPED_TIME, "metadata_with_label.feather"
    )
    time_consume = [100] * 100 + [1000] * 100

    resize_l = 1024
    K = 5
    stroke_num = 8
    patch_size = 32

    model, meta_brushes, device = init()

    df = pd.read_feather(file_path)
    img_paths = base_path + df["img_path"]

    for img_path in tqdm(img_paths):
        save_path = img_path.split(".")[0] + "_ani-test.webp"
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
        break


if __name__ == "__main__":
    img2ani()
# TODO duration 조절