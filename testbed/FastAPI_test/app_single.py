from fastapi import FastAPI
from PaintTransformer.inference import init, inference
from PIL import Image
import base64
import io

# Create a FastAPI instance
app = FastAPI()

# model initialization
model, meta_brushes, device = init()


def from_image_to_bytes(img, ext):
    """
    pillow image 객체를 bytes로 변환
    """
    # Pillow 이미지 객체를 Bytes로 변환
    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format=ext)
    imgByteArr = imgByteArr.getvalue()
    # Base64로 Bytes를 인코딩
    encoded = base64.b64encode(imgByteArr)
    return encoded


def from_bytes_to_image(bytes):
    return Image.open(io.BytesIO(base64.b64decode(bytes)))


@app.post("/")
async def get_image(img_encoded: str):
    """dataset directory에 있는 이미지의 정보를 df 형식으로 변환
    Args:
        img_encoded (str): FastAPI가 수신받는 image data
    Returns:
        image_bytes (str): FastAPI가 리턴하는 image data
    """
    img = from_bytes_to_image(img_encoded)
    img_list = inference(
        image=img,
        device=device,
        model=model,
        meta_brushes=meta_brushes,
    )
    image_bytes = from_image_to_bytes(img_list[-1], "WEBP")
    response = {"image": image_bytes}
    return response


# @app.post("/")
# async def get_image(test_str: str):
#     """dataset directory에 있는 이미지의 정보를 df 형식으로 변환
#     Args:
#         img_encoded (str): FastAPI가 수신받는 image data
#     Returns:
#         image_bytes (str): FastAPI가 리턴하는 image data
#     """
#     # img = from_bytes_to_image(img_encoded)
#     # img_list = inference(
#     #     image=img,
#     #     device=device,
#     #     model=model,
#     #     meta_brushes=meta_brushes,
#     # )
#     # image_bytes = from_image_to_bytes(img_list[-1], "WEBP")
#     response = {"image": '1'}
#     return response


# uvicorn app:app --reload
# uvicorn app_single:app --reload --host=0.0.0.0 --port=30001