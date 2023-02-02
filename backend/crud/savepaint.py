from sqlalchemy.orm import Session
from sqlalchemy import and_
from fastapi import HTTPException


from utils import LOGGER
from model import *
from scheme import *

def read_category(db: Session, category: str):
    """category에 맞는 데이터 읽음

    Args:
        db (Session): DB
        category (str): 카테고리

    """
    try:
        img_paths = db.query(GameData).filter(GameData.category == category).all()
    except Exception as e:
        LOGGER.error(e)
        return HTTPException(status_code=500, detail="DB ERROR(please check category, img_path)")
    
    return img_paths


def read_category_and_path(db: Session, path: str, category: str):
    try:
        data = db.query(GameData).filter(and_(GameData.category == category, GameData.img_path == path)).first()
    except Exception as e:
        LOGGER.error(e)
        return HTTPException(status_code=500, detail="DB ERROR(please check category, img_path)")
    return data


def create_from_df(db: Session, df, category):
    datas = []
    for idx, row in df.iterrows():
        datas.append(
            GameData(
                created_time=row.crawled_time,
                tag=row.tag,
                label=row.label,
                category=category,
                img_height=row.img_height,
                img_width=row.img_width,
                img_path=row.img_path
            )
        )
    db.add_all(datas)
    db.commit()
    LOGGER.debug("add crawling data to DB")
    
