from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse, FileResponse, Response, JSONResponse

from utils import set_game_imgs, get_paint_img, get_result_imgs, get_origin_imgs
from scheme import *

router = APIRouter()

    
@router.post('/gamestart')
async def gamestart(game_in: GameIn):
    img_paths = set_game_imgs(game_in.category)
    return JSONResponse(content={"img_list" : img_paths})
    

@router.post('/paint')
async def paint(path: ImagePath):
    
    return StreamingResponse(
        content=get_paint_img(path.path),
        media_type='images/gif'
    )


@router.post('/result', response_model=GameOut)
async def result(paths: ImagePaths):
    
    result_imgs = get_result_imgs(paths.paths)
    origin_imgs = get_origin_imgs(paths.paths)

    return {
        "result_imgs": result_imgs,
        "origin_imgs": origin_imgs
    }