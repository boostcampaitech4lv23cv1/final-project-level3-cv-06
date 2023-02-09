import base64
import io
import logging
import uuid

from google.cloud import storage
from google.oauth2 import service_account

from sqlalchemy.orm import Session
from db import get_db
from model import Score
from fastapi import Depends


KEY_PATH = 'env/key_v1.json'
bucket_name = "scraped-img"

credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
client = storage.Client(credentials = credentials, project = credentials.project_id)
bucket = client.bucket(bucket_name)


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
    if extend == "jpg" or extend == "JPG":
        extend = "jpeg"

    imgByteArr = io.BytesIO()
    img.save(imgByteArr, format=extend)
    # img.save(imgByteArr, format="PNG")
    imgByteArr = imgByteArr.getvalue()
    # Base64로 Bytes를 인코딩
    encoded = base64.b64encode(imgByteArr)  # byte
    # Base64로 utf-8로 디코딩
    decoded = encoded.decode("utf-8")  #
    print(decoded)
    return decoded

    
def save_user_img(img, file_name):
    # PIL image 받아서 WEBP로 저장
    webp_io = io.BytesIO()
    img.save(webp_io, format="WEBP")
    blob = bucket.blob(f'user_img/{file_name}_{uuid.uuid1()}.webp')
    blob.upload_from_string(webp_io.getvalue(), content_type="image/webp")
    LOGGER.info('save user image to GCS')
    

def set_logger(name):
    logger = logging.getLogger(name)
    formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)s - %(funcName)s - %(levelname)s - %(message)s')
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(name + ".log", encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

LOGGER = set_logger('app')


def user_name_check(name, db: Session = Depends(get_db)):
    exist = db.query(Score).filter(Score.user_name == name).first()
    if exist:
        return False
    else:
        return True
    
    
