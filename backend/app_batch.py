# app.py
import pandas as pd
from fastapi import FastAPI
from fastapi import File
from fastapi import FastAPI
from schemas import PredIn
from PaintTransformer.inference_batch import init, inference
import os
import numpy as np
import cv2
from PIL import Image
import random
import base64
import io
import time

from fastapi import UploadFile

# Create a FastAPI instance
app = FastAPI()

model_path="PaintTransformer/model.pth"

resize_l = 256

K = 4

stroke_num = 8
patch_size = 32

model, meta_brushes, device = init(stroke_num, model_path="PaintTransformer/model.pth")

def predict_batch(img):

    # input_path = "input"
    # path_list = os.listdir(input_path)

    # selected = random.sample(path_list, 1)[0]
    # input_path = os.path.join(input_path, selected)

    # origin_image = cv2.imread(input_path)
    # origin_image = cv2.cvtColor(origin_image, cv2.COLOR_BGR2RGB)
    # origin_image = origin_image.tolist()

    # output_dir_root= "output/"

    # label = selected.split("_")[0]
    start = time.time()

    pred = inference(
        model,
        device,
        meta_brushes,
        image=img,
        stroke_num=stroke_num,
        patch_size=patch_size,
        K=K,
        need_animation=True,        # whether need intermediate results for animation.
        resize_l=resize_l,          # resize original input to this size. (max(w, h) = resize_l)
        serial=True,                # if need animation, serial must be True.
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

    return buffer


@app.post("/")  # , response_model=PredOut)
async def get_image(img_encoded):
    img = Image.open(io.BytesIO(base64.b64decode(img_encoded)))
    print(img.size)
    print(type(img))
    print(img)
    res = predict_batch(img)
    response = {"image": res}
    return response
