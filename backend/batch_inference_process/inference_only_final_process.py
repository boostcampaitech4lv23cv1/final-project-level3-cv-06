from PIL import Image
import requests
import base64
import io


def from_image_to_bytes(img):
    """
    pillow image 객체를 bytes로 변환
    """
    # Pillow 이미지 객체를 Bytes로 변환
    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format=img.format)
    imgByteArr = imgByteArr.getvalue()
    # Base64로 Bytes를 인코딩
    encoded = base64.b64encode(imgByteArr)
    # Base64로 ascii로 디코딩
    decoded = encoded.decode("ascii")
    return decoded


img = Image.open("../PaintTransformer/dataset/original/animal/cat/cat_1.jpg")
img_encoded = from_image_to_bytes(img)

params = {"img_encoded": img_encoded}
response = requests.post(f"http://127.0.0.1:8000", params=params).json()

image = response["image"]
Image.open(io.BytesIO(base64.b64decode(image)))
myimagedata = base64.b64decode(image)
myimagefile = open("output.jpg", "wb")
myimagefile.write(myimagedata)
myimagefile.close()
