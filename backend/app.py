# app.py
import pandas as pd
from fastapi import FastAPI
from fastapi import File
from fastapi import FastAPI
from schemas import PredIn
from PaintTransformer.inference import main
import os
import numpy as np
import cv2
from PIL import Image
import random
import base64
import io
import time
import uvicorn
from schemas import PredIn, GameIn
from starlette.middleware.cors import CORSMiddleware
import imageio

# Create a FastAPI instance
app = FastAPI()

origins = [
    "http://localhost:8080/game",
    "http://192.168.55.139:8080/game",
    "http://192.168.55.139:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def predict(category):
    input_path = os.path.join("input", category)
    path_list = os.listdir(input_path)

    selected = random.sample(path_list, 1)[0]
    input_path = os.path.join(input_path, selected)

    origin_image = cv2.imread(input_path)
    origin_image = cv2.cvtColor(origin_image, cv2.COLOR_BGR2RGB)
    origin_image = origin_image.tolist()

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

    return buffer, label, origin_image


@app.post("/")  # , response_model=PredOut)
async def get_image(info: PredIn):
    # res, label = predict(info["category"])
    res, label, origin_image = predict(info.category)
    response = {"image": res, "label": label, "origin_image": origin_image}
    return response


@app.get("/")
def test():
    return {"messege": "success"}


@app.post("/gamestart")
async def img_return(info: GameIn):
    img_path = os.listdir("img")
    img_path = random.sample(img_path, 9)
    gif_path = []
    answer_list = []
    for path in img_path:
        answer_list.append(path.split(".")[0])
        gif_path.append(path.split(".")[0] + ".gif")
    img_list = []
    gif_list = []
    for img in img_path:
        img = "img/" + img
        tmp = cv2.imread(img)
        # tmp = cv2.cvtColor(tmp, cv2.COLOR_BGR2RGB)
        _, buffer = cv2.imencode(".jpg", tmp)
        img_list.append(base64.b64encode(buffer))
    for gif in gif_path:
        gif = "gif/" + gif
        with open(gif, "rb") as image_file:
            gif_list.append(base64.b64encode(image_file.read()))

    response = {"origin_img": img_list, "paint_img": gif_list, "answer": answer_list}
    print(len(img_list))
    return response
