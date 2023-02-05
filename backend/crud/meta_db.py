from sqlalchemy.orm import Session
from sqlalchemy import and_
from fastapi import HTTPException

from utils import LOGGER
from model import *
from scheme import *

def read_no_label_and_using(db: Session, category: str):
    """ 카테고리에 맞는 label없고 사용가능한 데이터 읽음
    
    """
    return db.query(GameData).filter(and_(GameData.category == category, GameData.label == "NaN", GameData.use_status == True)).all()


def read_category(db: Session, category: str):
    """category에 맞는 모든 데이터 읽음

    """
    try:
        img_paths = db.query(GameData).filter(and_(GameData.category == category)).all()
    except Exception as e:
        LOGGER.error(e)
        return HTTPException(status_code=500, detail="DB ERROR(please check category)")
    
    return img_paths