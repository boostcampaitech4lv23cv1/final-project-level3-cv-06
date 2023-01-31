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


@router.post('/gameover')
async def gameover(game_over: GameOver, db: Session = Depends(get_db)) -> List:

    table = game_over.category
    
    for path, correct in zip(game_over.img_paths, game_over.correct_list):
        if table == "animal":
            db_game = db.query(Animal).filter(Animal.img_path == path).first()
        elif table == "landmark":
            db_game = db.query(Landmark).filter(Landmark.img_path == path).first()
        elif table == "celebrity":
            db_game = db.query(Celebrity).filter(Celebrity.img_path == path).first()
        else:
            ValueError("잘못된 카테고리가 입력되었습니다.")
            
        if correct:
            db_game.correct_cnt += 1
        else:
            db_game.incorrect_cnt += 1
            
    db.commit()
    
    return {"rank": 0}
    