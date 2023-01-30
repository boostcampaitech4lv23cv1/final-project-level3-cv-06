import os
import cv2
import time
import random
import base64
import io
from glob import glob
from PIL import Image
import numpy as np

from google.cloud import storage
from google.oauth2 import service_account

from typing import List

from PaintTransformer.inference import init, inference
from PaintTransformer.inference_only_final import inference as inference_by_img

KEY_PATH = 'env/key.json'
DATA_PATH = 'dataset'
model_path = "PaintTransformer/model.pth" # main.py 기준으로 경로 설정해야 함
bucket_name = "image_cloud_demo"

credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
client = storage.Client(credentials = credentials, project = credentials.project_id)
bucket = client.bucket(bucket_name)

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
        resize_l=resize_l,          # resize original input to this size. (max(w, h) = resize_l)
        serial=False,                # if need animation, serial must be True.
    )

    return final_img


def from_image_to_bytes(img, extend):
    """
    pillow image 객체를 bytes로 변환
    """
    # Pillow 이미지 객체를 Bytes로 변환
    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format=extend)
    imgByteArr = imgByteArr.getvalue()
    encoded = base64.b64encode(imgByteArr)
    return encoded


def from_image_to_str(img, extend):
    """
    pillow image 객체를 bytes로 변환
    """
    if extend == "jpg":
        extend = "jpeg"

    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format=extend)
    # img.save(imgByteArr, format="PNG")
    imgByteArr = imgByteArr.getvalue()
    # Base64로 Bytes를 인코딩
    encoded = base64.b64encode(imgByteArr) # byte
    # Base64로 utf-8로 디코딩
    decoded = encoded.decode('utf-8') # 
    return decoded

    
def save_user_img(img, file_name):
    # PIL image 받아서 WEBP로 저장
    img.save(f"{file_name}.webp", format="WEBP")
