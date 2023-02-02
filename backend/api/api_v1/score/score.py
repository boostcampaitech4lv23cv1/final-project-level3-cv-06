from fastapi import APIRouter, HTTPException, Depends, File, UploadFile, BackgroundTasks
from fastapi.responses import StreamingResponse


from sqlalchemy.orm import Session
from typing import List
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

@router.post('')
async def create(score_in: ScoreIn, db: Session = Depends(get_db)):
    # validation check
    # valid = user_name_check(score_in.user_name, db)
    # if not valid:
    #     return HTTPException(status_code=400, detail="user name already exists")
    create_score(db, score_in.user_name, score_in.play_time, score_in.correct_cnt)
    


@router.get('', response_model=List[ScoreOut])
async def read_score(db: Session = Depends(get_db)):
    data = read_all_score(db)
    return data
    
    
    
    
    
