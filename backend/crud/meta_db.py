from sqlalchemy.orm import Session
from sqlalchemy import and_
from fastapi import HTTPException

from utils import LOGGER
from model import *
from scheme import *

def read_no_label_and_using(db: Session):
    return db.query(GameData).filter(and_(GameData.label == "NaN", GameData.use_status == True)).all()


def read_category(db: Session, category: str):
    """category에 맞는 데이터 읽음

    Args:
        db (Session): DB
        category (str): 카테고리

    """
    try:
        img_paths = db.query(GameData).filter(and_(GameData.category == category)).all()
    except Exception as e:
        LOGGER.error(e)
        return HTTPException(status_code=500, detail="DB ERROR(please check category)")
    
    return img_paths