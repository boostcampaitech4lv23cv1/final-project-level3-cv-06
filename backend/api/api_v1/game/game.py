from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse, FileResponse, Response, JSONResponse

from utils import get_img, from_image_to_bytes
from scheme import *

router = APIRouter()

@router.post('/gamestart')
async def gamestart(game_in: GameIn):
    # 나중에 GCP Path보내는 걸로 교체할 것
    paint_imgs, origin_imgs, result_imgs, answers = get_img(game_in.category)
    return JSONResponse(content={
        "answer": answers,
        "paint_img": paint_imgs,
        "origin_img": origin_imgs,
        "result_img": result_imgs
        }, 
        media_type="application/json")
    

@router.post('/gameover')
async def gameover():
    # TODO
    # 점수 받아서 DB에 저장하기
    pass