import io
import logging
from google.cloud import storage
from google.oauth2 import service_account
import uuid
from pytz import utc, timezone
from datetime import datetime


KEY_PATH = 'env/key.json'
bucket_name = "scraped-img"
credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
client = storage.Client(credentials = credentials, project = credentials.project_id)
bucket = client.bucket(bucket_name)


def timetz(*args):
    utc_dt = utc.localize(datetime.utcnow())
    tz = timezone("Asia/Seoul")
    converted = utc_dt.astimezone(tz)
    return converted.timetuple()


def set_logger(name):
    logger = logging.getLogger(name)
    logging.Formatter.converter = timetz
    formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)s - %(levelname)s - %(message)s')
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(name + ".log", encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger

LOGGER = set_logger("infer")

def save_user_img(img, file_name):
    # PIL image 받아서 WEBP로 저장
    webp_io = io.BytesIO()
    img.save(webp_io, format="WEBP")
    blob = bucket.blob(f'user_img/{file_name}_{uuid.uuid1()}.webp')
    blob.upload_from_string(webp_io.getvalue(), content_type="image/webp")
    LOGGER.info('save user image to GCS')
    

def is_valid(resize_l, K, stroke_num, mode):

    valid = False
    try:
        assert 32 <= resize_l <= 1024
        assert 2<= K <= 6
        assert mode == "small" or mode == "large"
        assert stroke_num == 6 or stroke_num == 8 or stroke_num == 12 or stroke_num == 16
    except Exception as e:
        LOGGER.error(e)
        return valid


   
    if 513 <= resize_l and 5 <= K:
        valid = True
    elif 257 <= resize_l and 4 <= K:
        valid = True
    elif 129 <= resize_l and 3 <= K:
        valid = True
    elif 32 <= resize_l and 2 <= K:
        valid = True
    
    return valid
    