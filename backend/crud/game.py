from sqlalchemy.orm import Session
from sqlalchemy import and_, text
from sqlalchemy.sql.expression import func, distinct
from fastapi import HTTPException

from utils import LOGGER
from model import *
from scheme import *


def read_game_data(db: Session, category: str):
    """category에 맞으면서 use status가 True인 데이터 읽음

    Args:
        db (Session): DB
        category (str): 카테고리

    """
    try:
        sql = text(
            "SELECT * "
            "FROM ( "
            "SELECT DISTINCT ON (label) * "
            "FROM game_data "
            "WHERE category = :category AND label != 'NaN' "
            "ORDER BY label, random() "
            ") t "
            "ORDER BY random() "
            "LIMIT 9;"
        )
        img_paths = db.execute(sql, {"category": category}).all()
    except Exception as e:
        LOGGER.error(e)
        return HTTPException(status_code=500, detail="DB ERROR(please check category)")
    
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
    try:
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
    except Exception as e:
        LOGGER.error(e)
    
