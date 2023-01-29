from io import BytesIO
import base64
from PIL import Image

from utils import predict_by_img, save_user_img
from fastapi import APIRouter, HTTPException, BackgroundTasks
from fastapi import FastAPI, File, UploadFile, Response
from fastapi.responses import FileResponse, JSONResponse

router = APIRouter()


@router.post("/")
async def inference(
    file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks()
):
    # print(uf.filename)
    file_name = file.filename
    extend = file_name.split('.')[-1]
    if extend == 'jpg':
        extend = 'jpeg'
        
    content = await file.read()
    bytes_data = BytesIO(content)
    img = Image.open(bytes_data)

    background_tasks.add_task(save_user_img, img, file_name)
    # gcs로 보내는 백그라운드 task 추가하기

    paint_img = predict_by_img(img)
    img_byte = BytesIO()
    paint_img.save(img_byte, format=extend)
    img_byte = img_byte.getvalue()
    encoded = base64.b64encode(img_byte)
    return Response(content=encoded)
