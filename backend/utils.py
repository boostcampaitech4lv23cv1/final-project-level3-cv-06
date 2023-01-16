import os
import cv2
import time
import random
import base64
import aiofiles
import io
from PIL import Image
import numpy as np

from PaintTransformer.inference import init, inference
from PaintTransformer.inference_only_final import inference as inference_by_img


model_path = "PaintTransformer/model.pth"  # main.py 기준으로 경로 설정해야 함

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

    output_dir_root = "output/"

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
        need_animation=True,  # whether need intermediate results for animation.
        resize_l=resize_l,  # resize original input to this size. (max(w, h) = resize_l)
        serial=True,  # if need animation, serial must be True.
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
        resize_l=resize_l,  # resize original input to this size. (max(w, h) = resize_l)
        serial=False,  # if need animation, serial must be True.
    )

    return final_img


def from_image_to_bytes(img):
    """
    pillow image 객체를 bytes로 변환
    """
    # Pillow 이미지 객체를 Bytes로 변환
    imgByteArr = io.BytesIO()
    # img.save(imgByteArr, format=img.format)
    img.save(imgByteArr, format="PNG")
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr


def from_image_to_str(uf, extend: str):
    """
    pillow image 객체를 bytes로 변환
    """
    # Pillow 이미지 객체를 Bytes로 변환
    imgByteArr = io.BytesIO()
    if extend == "jpg":
        extend = "jpeg"
    uf.save(imgByteArr, format=extend)
    # img.save(imgByteArr, format="PNG")
    imgByteArr = imgByteArr.getvalue()
    # Base64로 Bytes를 인코딩
    encoded = base64.b64encode(imgByteArr)
    # Base64로 ascii로 디코딩
    # decoded = encoded.decode('ascii')
    return encoded


async def save_img(uf):

    # async with aiofiles.open(out_file_path, 'wb') as out_file:
    #     while content := await in_file.read(1024):  # async read chunk
    #         await out_file.write(content)  # async write chunk

    # try: # db저장 필요
    #     async with aiofiles.open('./raw_image/test.jpg', 'wb') as out_file: # 받은 사진 저장
    #         content = await img_b.read()  # async read
    #         await out_file.write(content)  # async write

    try:  # db 저장 필요
        # aiofiles사용시 오류남
        with open(f"./raw_image/{uf.filename}", "wb") as out_file:  # 받은 사진 저장
            await uf.seek(0)
            content = await uf.read()  # async read
            out_file.write(content)  # async write
    except Exception as e:
        print(f"ERROR: {e}")
        print("저장 실패")
    finally:
        print("save image")
