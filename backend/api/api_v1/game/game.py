from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse

from sqlalchemy.orm import Session
from typing import List

from utils import *
from scheme import *
from crud import *
from db import *


router = APIRouter()
    
    
@router.post('/gamestart', response_model=List[SavePaintOut])
async def gamestart(game_start: GameStart, db: Session = Depends(get_db)) -> List:
    img_paths = read_savepaint(db, game_start.category)
    LOGGER.info('someone start game')
    return random.sample(img_paths, 9)


@router.post('/gameover', response_model=List[SavePaintOut])
async def gameover(game_over: GameOver, db: Session = Depends(get_db)) -> List:
    pass