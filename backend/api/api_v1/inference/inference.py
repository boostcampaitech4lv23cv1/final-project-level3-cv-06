from io import BytesIO
import base64
import time
import requests as rq
from PIL import Image

from utils import predict_by_img, save_user_img, LOGGER
from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi import File, UploadFile, Response

router = APIRouter()
router.redirect_slashes = False

@router.post("", include_in_schema=False)
async def inference(
    file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks(), 
    ):
    """
    사용자의 사진 Inference 진행 및 백그라운드 작업으로 GCS에 사진 저장\n
    현재 사용 안함
    """
    # 사진 하나만 가능
    # print(uf.filename)
    file_name = file.filename
    extend = file_name.split(".")[-1]
    if extend == "jpg" or extend == "JPG":
        extend = "jpeg"
        
    content = await file.read()
    bytes_data = BytesIO(content)
    img = Image.open(bytes_data)

    # gcs로 보내는 task로 변경할 것
    background_tasks.add_task(save_user_img, img, file_name)
    
    try:
        start_time = time.time()
        paint_img = predict_by_img(img)
        img_byte = BytesIO()
        paint_img.save(img_byte, format=extend)
        img_byte = img_byte.getvalue()
        encoded = base64.b64encode(img_byte)
        
        LOGGER.debug(f"Inference(process time: {time.time() - start_time})")
        return Response(content=encoded)
    except Exception as e:
        LOGGER.error(e)
        return Response(status_code="500")
    
