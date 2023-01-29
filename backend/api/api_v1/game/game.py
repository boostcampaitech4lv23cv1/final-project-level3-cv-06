from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse

from sqlalchemy.orm import Session
from typing import List

from utils import *
from scheme import *
from crud import *
from db import *


Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get('/create')
def create_dummy(db: Session = Depends(get_db)):
    # dummy data 생성 추후 삭제 필요
    create_dummy_data(db)
    return {'messege':'success'}
    
    
@router.post('/gamestart', response_model=List[SavePaintOut])
async def gamestart(game_start: GameStart, db: Session = Depends(get_db)) -> List:
    img_paths = read_savepaint(db, game_start.category)
    return random.choice(img_paths, 9)


@router.post('/gameover', response_model=List[SavePaintOut])
async def gameover(game_over: GameOver, db: Session = Depends(get_db)) -> List:
    pass