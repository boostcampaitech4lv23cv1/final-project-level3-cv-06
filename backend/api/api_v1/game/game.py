from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session
from typing import List

from utils import *
from scheme import *
from crud import *
from db import *


router = APIRouter()
    
    
@router.post('/gamestart', response_model=List[SavePaintOut])
async def gamestart(game_start: GameStart, db: Session = Depends(get_db)) -> List:
    """게임 시작 시 카테고리에 맞는 gcs경로 랜덤으로 전송

    Args:
        game_start (GameStart): game start 
        db (Session, optional): DB. Defaults to Depends(get_db).

    Returns:
        List: 랜덤한 경로
    """
    
    img_paths = read_category(db, game_start.category)
    LOGGER.info('someone start game')
    return random.sample(img_paths, 9)


@router.post('/gameover')
async def gameover(game_over: GameOver, db: Session = Depends(get_db)):
    """게임 종료시 이미지 정답, 오답 기록
    
    """
    category = game_over.category
    for path, correct in zip(game_over.img_paths, game_over.correct_list):
        data = read_category_and_path(db, path, category)
        if correct:
            data.correct_cnt += 1
        else:
            data.incorrect_cnt += 1
            
    db.commit()
    