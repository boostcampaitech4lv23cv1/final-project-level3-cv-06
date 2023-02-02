from sqlalchemy.orm import Session
from fastapi import HTTPException
import random

from datetime import datetime, date

from model import *
from scheme import *

def read_savepaint(db: Session, category: str):
    """category에 맞는 데이터 읽음

    Args:
        db (Session): DB
        category (str): 카테고리

    """
    try:
        img_paths = db.query(GameData).filter(GameData.category == category).all()
    except:
        return HTTPException(status_code=400, detail="존재하지 않는 카테고리입니다")
    
    return img_paths

def create_dummy_data(db):
    # animal, landmark, celebrity 테이블 생성 => init.d에서 완료
    # 테이블에 데이터 추가
    # BasePath = "https://storage.googleapis.com/image_cloud_demo/"

    data = []
    
    paths = [
        "animal/pixabay/07-18/00001_origin.webp",
        "animal/pixabay/07-18/00002_origin.webp",
        "animal/pixabay/07-18/00003_origin.webp",
        "animal/pixabay/07-18/00004_origin.webp",
        "animal/pixabay/07-18/00005_origin.webp",
        "animal/pixabay/07-18/00006_origin.webp",
        "animal/pixabay/07-18/00007_origin.webp",
        "animal/pixabay/07-18/00008_origin.webp",
        "animal/pixabay/07-18/00009_origin.webp",
        "landmark/pixabay/08-15/00001_origin.webp",
        "landmark/pixabay/08-15/00002_origin.webp",
        "landmark/pixabay/08-15/00003_origin.webp",
        "landmark/pixabay/08-15/00004_origin.webp",
        "landmark/pixabay/08-15/00005_origin.webp",
        "landmark/pixabay/08-15/00006_origin.webp",
        "landmark/pixabay/08-15/00007_origin.webp",
        "landmark/pixabay/08-15/00008_origin.webp",
        "landmark/pixabay/08-15/00009_origin.webp",
        "celebrity/pixabay/08-16/00001_origin.webp",
        "celebrity/pixabay/08-16/00002_origin.webp",
        "celebrity/pixabay/08-16/00003_origin.webp",
        "celebrity/pixabay/08-16/00004_origin.webp",
        "celebrity/pixabay/08-16/00005_origin.webp",
        "celebrity/pixabay/08-16/00006_origin.webp",
        "celebrity/pixabay/08-16/00007_origin.webp",
        "celebrity/pixabay/08-16/00008_origin.webp",
        "celebrity/pixabay/08-16/00009_origin.webp",
    ]
    
    # show server_encoding, client_encoding 기본값이 UTF-8
    labels = [
        "알파카",
        "고양이",
        "병아리",
        "닭",
        "개",
        "사자",
        "토끼",
        "달팽이",
        "호랑이",
        "빅벤",
        "부다페스트",
        "콜로세움",
        "에펠탑",
        "롯데타워",
        "오페라하우스",
        "피사의사탑",
        "타지마할",
        "타워브릿지"
    ]
    for label, path in zip(labels, paths):
        category = path.split('/')[0]
        if category == "animal":
            data.append(
                Animal(
                    created_time=date.today(),
                    label=label,
                    img_path=path
                )
            )
        elif category == "landmark":
            data.append(
                Landmark(
                    created_time=date.today(),
                    label=label,
                    img_path=path
                )
            )
        elif category == "celebrity":
            data.append(
                Celebrity(
                    created_time=date.today(),
                    label=label,
                    img_path=path
                )
            )
        else:
            raise ValueError("없는 카테고리 입니다")
        
    db.add_all(data)
    db.commit()