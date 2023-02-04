from datetime import datetime

from sqlalchemy.orm import Session

from model import *
from scheme import *

def read_all_score(db: Session):
    """
    correct_cnt 내림차순
    play_time 오름차순
    """
    return db.query(Score).order_by(Score.correct_cnt.desc(), Score.play_time.asc()).all()

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