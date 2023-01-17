# app.py
from fastapi import FastAPI
from fastapi import File
from fastapi import FastAPI
from PaintTransformer.inference_only_final import init, inference
from PIL import Image
import base64
import io

# Create a FastAPI instance
app = FastAPI()

# parameters
model_path="PaintTransformer/model.pth"
stroke_num = 8
resize_l = 256
K = 4
patch_size = 32

# model initialization
model, meta_brushes, device = init(stroke_num, model_path="PaintTransformer/model.pth")

def from_image_to_bytes(img):
    """
    pillow image 객체를 bytes로 변환
    """
    # Pillow 이미지 객체를 Bytes로 변환
    imgByteArr = io.BytesIO()
    # img.save(imgByteArr, format=img.format)
    img.save(imgByteArr, format="JPEG")
    imgByteArr = imgByteArr.getvalue()
    # Base64로 Bytes를 인코딩
    encoded = base64.b64encode(imgByteArr)
    # Base64로 ascii로 디코딩
    decoded = encoded.decode('ascii')
    return decoded


@app.post("/")
async def get_image(img_encoded: str):
    """dataset directory에 있는 이미지의 정보를 df 형식으로 변환
    Args:
        img_encoded (str): FastAPI가 수신받는 image data, 
    Returns:
    """
    img = Image.open(io.BytesIO(base64.b64decode(img_encoded)))
    _, only_final = inference(
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
    image_bytes = from_image_to_bytes(only_final)
    response = {"image": image_bytes}
    return response
