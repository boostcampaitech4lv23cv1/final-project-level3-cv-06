from sqlalchemy.orm import Session

import random

from datetime import datetime

from model import *
from scheme import *

def read_savepaint(db: Session, category: str):
    # 없는 테이블 가져올 경우 예외 처리
    # 테이블 이름(=카테고리 이름)으로 전체 row 가져오는 방법 찾기
    img_paths = db.query(Animal).all()
    return img_paths

def create_dummy_data(db):
    data_lst = []
    
    labels = [
        "alpaca",
        "cat",
        "chick",
        "chicken",
        "dog",
        "lion",
        "rabbit",
        "snail",
        "tiger"
    ]
    paths = [
        "https://storage.googleapis.com/image_cloud_demo//original/animal/alpaca/alpaca_0.jpg",
        "https://storage.googleapis.com/image_cloud_demo//original/animal/cat/cat_1.jpg",
        "https://storage.googleapis.com/image_cloud_demo//original/animal/chick/chick_01.jpg",
        "https://storage.googleapis.com/image_cloud_demo//original/animal/chicken/chicken_01.jpg",
        "https://storage.googleapis.com/image_cloud_demo//original/animal/dog/dog_1.jpg",
        "https://storage.googleapis.com/image_cloud_demo//original/animal/lion/lion_01.jpg",
        "https://storage.googleapis.com/image_cloud_demo//original/animal/rabbit/rabit_1.jpg",
        "https://storage.googleapis.com/image_cloud_demo//original/animal/snail/snail_01.jpg",
        "https://storage.googleapis.com/image_cloud_demo//original/animal/tiger/tiger_01.jpg"
    ]
    
    for label, path in zip(labels, paths):
        data_lst.append(Animal(
            created_time=datetime.now(),
            category='animal',
            label=label,
            img_height=300,
            img_width=300,
            img_path=path,
            correct_cnt=0,
            incorrect_cnt=0
        ))
    db.add_all(data_lst)
    db.commit()