from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy import and_
from fastapi import HTTPException


from utils import LOGGER
from model import *
from scheme import *

def read_all_score(db: Session):
    return db.query(Score).all().order_by(Score.correct_cnt.desc(), Score.play_time.asc())

def create_score(db: Session, user_name, play_time, correct_cnt):
    now = datetime.now()
    score = Score(
                created_time = now.strftime('%Y-%m-%d %H:%M:%S'),
                user_name = user_name,
                play_time = play_time,
                correct_cnt = correct_cnt
            )
    db.add(score)
    db.commit()