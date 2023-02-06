import random
from collections import defaultdict

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
    """
    게임 시작 API\n
    GCS로 부터 전체 경로를 받아 다른 9개 레이블 랜덤으로 받아서 리스트로 전송

    **game_start**
    - category: str
    """
    
    items = read_game_data(db, game_start.category)
    try: # 로직 수정 필요
        result = []
        data_dict = defaultdict(list)
        for item in items:
            data_dict[item.label] = item
            
        random_keys = random.choices(list(data_dict.keys()), k=9)
        
        for key in random_keys:
            result.append(random.choice(list(data_dict[key])))
        
        return result
    except Exception as e:
        LOGGER.error(e)
        return HTTPException(status_code="500", detail="아직 게임이 준비되지 않았습니다.(The number of category is under 9)")

    return random_list


@router.post('/gameover')
async def gameover(game_over: GameOver, db: Session = Depends(get_db)):
    """
    게임 종료시 이미지 정답, 오답 여부 DB에 기록
    
    **game_over**
    - category: str
    - img_paths: list[str]
    - correct_list: list[str]
    
    """
    category = game_over.category
    for path, correct in zip(game_over.img_paths, game_over.correct_list):
        data = read_category_and_path(db, path, category)
        if correct:
            data.correct_cnt += 1
        else:
            data.incorrect_cnt += 1
        db.commit()
    
