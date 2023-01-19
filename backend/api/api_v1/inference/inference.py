from io import BytesIO
import base64
from PIL import Image

from utils import predict_by_img, from_image_to_bytes, from_image_to_str, save_img
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
    background_tasks.add_task(save_img, file)

    content = await file.read()
    bytes_data = BytesIO(content)
    img = Image.open(bytes_data)
    paint_img = predict_by_img(img)
    img_byte = BytesIO()
    paint_img.save(img_byte, format=extend)
    img_byte = img_byte.getvalue()
    encoded = base64.b64encode(img_byte)
    return JSONResponse(content={"painte_img": encoded})
