import numpy as np
import torch
import time
from io import BytesIO
import base64
import pytz

from fastapi import FastAPI, UploadFile, File, Response, HTTPException, BackgroundTasks, Body
from fastapi.middleware.cors import CORSMiddleware

from utils import LOGGER, is_valid, save_user_img
from PaintTransformer.inference import *


app = FastAPI(
    docs_url='/api/v1/infer/docs',
    redoc_url='/api/v1/infer/redoc',
    openapi_url='/api/v1/infer/openapi.json'
)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/v1/infer")
async def infer(
    file: UploadFile = File(...),
    resize_l: int = Body(),
    backgroud_task :BackgroundTasks = BackgroundTasks()):
    """
    받은 이미지 PaintTransfer를 통해 inference
    
    **file**: image
    
    ***
    - resize_l: int
    
    """
    K = 5
    stroke_num = 8
    mode = "large"
    
    if not is_valid(resize_l, K, stroke_num, mode):
        return HTTPException(status_code="400", detail="파라미터를 확인해주세요")
    
    
    model, meta_brushes, device = init(
        stroke_num=stroke_num,
        model_path=f"model_{stroke_num:02d}.pth", 
        mode=mode)
    
    file_name = file.filename
    extend = file_name.split(".")[-1]
    if extend == "jpg" or extend == "JPG":
        extend = "jpeg"
    
        
    content = await file.read()
    bytes_data = BytesIO(content)
    img = Image.open(bytes_data)
    start_time = time.time()
    
    backgroud_task.add_task(save_user_img, img, file_name)
    
    try:
        output = inference(
            image=img,
            resize_l=resize_l,  # resize original input to this size. (max(w, h) = resize_l)
            K=K,  # set K
            device=device,
            model=model,
            meta_brushes=meta_brushes,
            stroke_num=stroke_num,
            patch_size=32,
        )
        img_byte = BytesIO()
        output.save(img_byte, format=extend)
        img_byte = img_byte.getvalue()
        encoded = base64.b64encode(img_byte)
        
        LOGGER.info(f"Infer Time: {time.time()-start_time}\n"
                     f"\t(resize_l: {resize_l}, K: {K}, stroke_num: {stroke_num}, device: {device})")
        return Response(content=encoded)
    except Exception as e:
        LOGGER.error(f"{e}")
        return Response(status_code="500")
    
    
    