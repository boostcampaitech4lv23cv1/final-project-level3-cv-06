from fastapi import APIRouter, HTTPException, Depends, File, UploadFile, BackgroundTasks
from fastapi.responses import StreamingResponse


from sqlalchemy.orm import Session
from typing import List, Union
from io import BytesIO
import pandas as pd
import time
from datetime import datetime

from utils import *
from scheme import *
from crud import *
from db import *

router = APIRouter()
router.redirect_slashes = False

@router.post('/create')
async def create(score_in: ScoreIn, db: Session = Depends(get_db)):
    """
    유저 점수 등록 API
    
    **socre_in**
    - user_name: str
    - play_time: float
    - correc_cnt: int
    
    """
    # validation check
    # valid = user_name_check(score_in.user_name, db)
    # if not valid:
    #     return HTTPException(status_code=400, detail="user name already exists")
    create_score(db, score_in.user_name, score_in.play_time, score_in.correct_cnt)
    LOGGER.debug('upload score')
    


@router.get('/read', response_model=List[ScoreOut])
async def read_score(db: Session = Depends(get_db)):
    """
    전체 점수 정보 가져오는 API

    ---
    
    Return
    - correct_cnt 높은 순
    - play_time 작은 순
    정렬 후 전송
    """
    
    data = read_all_score(db)
    return data
    
    
    
    
    
