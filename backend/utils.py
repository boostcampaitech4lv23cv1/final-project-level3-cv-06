import os
import cv2
import time
import random
import base64
import io
from PIL import Image
import numpy as np

from PaintTransformer.inference import init, inference
from PaintTransformer.inference_only_final import inference as inference_by_img


model_path="PaintTransformer/model.pth" # main.py 기준으로 경로 설정해야 함

resize_l = 256
K = 4
stroke_num = 8
patch_size = 32

model, meta_brushes, device = init(stroke_num, model_path=model_path)

def predict(category):

    input_path = os.path.join("input", category)
    path_list = os.listdir(input_path)

    selected = random.sample(path_list, 1)[0]
    input_path = os.path.join(input_path, selected)

    origin_image = cv2.imread(input_path)
    origin_image = cv2.cvtColor(origin_image, cv2.COLOR_BGR2RGB)
    origin_image = origin_image.tolist()

    output_dir_root= "output/"

    label = selected.split("_")[0]
    # start = time.time()

    pred = inference(
        model,
        device,
        meta_brushes,
        input_path=input_path,
        output_dir=output_dir_root,
        stroke_num=stroke_num,
        patch_size=patch_size,
        K=K,
        need_animation=True,        # whether need intermediate results for animation.
        resize_l=resize_l,          # resize original input to this size. (max(w, h) = resize_l)
        serial=True,                # if need animation, serial must be True.
    )

    # print(time.time() - start)
    buffer = io.BytesIO()
    pred = pred.transpose((0, 2, 3, 1))
    pred = (255 * np.clip(pred, 0, 1)).astype(np.uint8)
    im = []
    for n in range(len(pred)):
        im.append(Image.fromarray(pred[n]))
    # start = time.time()
    im[0].save(
        buffer,
        format="GIF",
        save_all=True,
        append_images=im[1:],
        optimize=True,
        duration=100,
    )
    # print(time.time() - start)
    buffer.seek(0)
    buffer = base64.b64encode(buffer.read()).decode()

    return buffer, label, origin_image

def predict_by_img(img):

    _, final_img = inference_by_img(
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

    return final_img