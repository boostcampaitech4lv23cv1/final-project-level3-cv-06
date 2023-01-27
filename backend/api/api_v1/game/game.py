from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse

from sqlalchemy.orm import Session
from typing import List

from utils import get_paint_img, get_result_imgs, get_origin_imgs
from scheme import *
from crud import *
from db import *


Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get('/create')
def create_dummy(db: Session = Depends(get_db)):
    create_dummy_data(db)
    return {'messege':'success'}
    
@router.post('/gamestart', response_model=List[SavePaintOut])
async def gamestart(game_in: GameIn, db: Session = Depends(get_db)):
    
    img_paths = read_savepaint(db, game_in.category)
    # random 추출
    return img_paths


@router.post('/paint_test')
async def paint(path: ImagePath):
    
    return StreamingResponse(
        content=get_paint_img(path.path),
        media_type='images/gif'
    )


@router.post('/result_test', response_model=GameOut)
async def result(paths: ImagePaths):
    
    result_imgs = get_result_imgs(paths.paths)
    origin_imgs = get_origin_imgs(paths.paths)

    return {
        "result_imgs": result_imgs,
        "origin_imgs": origin_imgs
    }