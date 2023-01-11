# app.py
import pandas as pd
from fastapi import FastAPI
from fastapi import File
from fastapi import FastAPI
from schemas import PredIn
from PaintTransformer.inference.inference import main
import os
import numpy as np
import cv2
from PIL import Image
import random
import base64
import io
import time

# Create a FastAPI instance
app = FastAPI()


def predict(category):
    input_path = os.path.join("input", category)
    path_list = os.listdir(input_path)

    selected = random.sample(path_list, 1)[0]
    input_path = os.path.join(input_path, selected)

    label = selected.split("_")[0]
    start = time.time()
    pred = main(
        input_path=input_path,
        model_path="PaintTransformer/inference/model.pth",
        output_dir="output/",
        need_animation=True,  # whether need intermediate results for animation.
        resize_h=256,  # resize original input to this size. None means do not resize.
        resize_w=256,  # resize original input to this size. None means do not resize.
        serial=True,
    )
    print(time.time() - start)
    buffer = io.BytesIO()
    pred = pred.transpose((0, 2, 3, 1))
    pred = (255 * np.clip(pred, 0, 1)).astype(np.uint8)
    im = []
    for n in range(len(pred)):
        im.append(Image.fromarray(pred[n]))
    start = time.time()
    im[0].save(
        buffer,
        format="GIF",
        save_all=True,
        append_images=im[1:],
        optimize=True,
        duration=100,
    )
    print(time.time() - start)
    buffer.seek(0)
    buffer = base64.b64encode(buffer.read()).decode()

    return buffer, label


@app.post("/")  # , response_model=PredOut)
async def get_image(info: str):
    # res, label = predict(info["category"])
    res, label = predict(info)
    response = {"image": res, "label": label}
    return response
