from io import BytesIO

import aiofiles
from fastapi import (
    APIRouter,
    BackgroundTasks,
    FastAPI,
    File,
    HTTPException,
    Response,
    UploadFile,
)
from fastapi.responses import FileResponse
from PIL import Image
from utils import from_image_to_bytes, from_image_to_str, predict_by_img, save_img

router = APIRouter()


@router.post("/")
async def inference(
    file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks()
):
    # print(uf.filename)
    file_name = file.filename
    extend = file_name.split(".")[-1]
    background_tasks.add_task(save_img, file)

    content = await file.read()
    bytes_data = BytesIO(content)
    img = Image.open(bytes_data)

    paint_img = predict_by_img(img)

    base64_img = from_image_to_str(paint_img, extend)
    return Response(content=base64_img)
