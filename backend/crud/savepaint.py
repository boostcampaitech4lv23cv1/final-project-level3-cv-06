from sqlalchemy.orm import Session
import random
from time import time

from model import *
from scheme import *

def read_savepaint(db: Session, category: str):
    img_paths = db.query(SavePaint).filter(SavePaint.category == category).all()
    return img_paths

def create_dummy_data(db):
    data_lst = []
    for i in range(1, 10):
        data_lst.append(SavePaint(
            created_time=time(),
            category='animal',
            label='cat',
            img_height=i*10,
            img_width=i*10,
            img_path=f"{i}.jpg"
        ))
    db.add_all(data_lst)
    db.commit()