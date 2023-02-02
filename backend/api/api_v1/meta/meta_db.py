from fastapi import APIRouter, HTTPException, Depends, File, UploadFile, BackgroundTasks, Body
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy import and_
from io import BytesIO
import pandas as pd

from utils import *
from scheme import *
from crud import *
from db import *

router = APIRouter()


@router.get('/test_create')
def create_dummy(db: Session = Depends(get_db)):
    # dummy data 생성 추후 삭제 필요
    create_dummy_data(db)
    return {'messege':'success'}


@router.get('/read', response_model=List[MetaDBOut])
def read_all_no_label(db: Session = Depends(get_db)):
    no_label_data = db.query(GameData).filter(and_(GameData.label == "", GameData.use_status == True)).all()
    return no_label_data


@router.post('/duplicate_check')
async def duplicate_check(
    id: str = Body(embed=True),
    category: str = Body(embed=True),
    db: Session = Depends(get_db)):
    """이미지 크롤링 하기 전 meta db에 같은 이미지가 있는지 확인하는 api

    Args:
        id (str, optional): 이미지 고유 아이디. Defaults to Body(embed=True).
        category (str, optional): 이미지 카테고리. Defaults to Body(embed=True).
        db (Session, optional): DB. Defaults to Depends(get_db).

    """
    
    valid = True
    table = db.query(GameData).filter(GameData.category == category).all()
    # TODO 리소스 줄이기
    # ordered로 받아 이분탐색 혹은 SQL문으로 한번에 가져오기
    for data in table:
        if data.img_path.split("/")[-1][:-5]==id:
            valid = False
            break
    
    if valid:
        return {"valid": True}
    else:
        return {"valid": False}
    

@router.post('/create')
async def crawling_create(
    file: UploadFile = File(),
    category: str = Body(),
    db: Session = Depends(get_db)):
    """_summary_

    Args:
        file (UploadFile, optional): feather 파일(data frame). Defaults to File().
        category (str, optional): 카테고리. Defaults to Body().
        db (Session, optional): DB. Defaults to Depends(get_db).

    """
    
    try:
        file_content = await file.read()
        data = pd.read_feather(BytesIO(file_content))
    except Exception as e:
        LOGGER.warning(e)
        return HTTPException(status_code=400, detail="file type error(please check whether file format is feather)")
    datas = []
    for idx, row in data.iterrows():
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
    
    return {"messege": "success"}
    

@router.post('/update')
async def crawling_update(
    file: UploadFile = File(),
    category: str = Body(),
    db: Session = Depends(get_db)):
    """ 추론 서버에서 추론 후 label 업데이트 하는 API

    Args:
        file (UploadFile, optional): feather file(pandas frame). Defaults to File().
        category (str, optional): 카테고리. Defaults to Body().
        db (Session, optional): DB. Defaults to Depends(get_db).

    """
    
    try:
        file_content = await file.read()
        data = pd.read_feather(BytesIO(file_content))
    except Exception as e:
        LOGGER.warning(e)
        return HTTPException(status_code=400, detail="file type error(please check whether file format is feather)")
        
    for idx, row in data.iterrows():
        db_item = db.query(GameData).filter(and_(GameData.category == category, GameData.img_path == row.img_path)).first()
        db_item.label = row.label
        db_item.use_status = row.use_status
    db.commit()
        
    return {"messege": "success"}


@router.post('/delete')
async def delete():
    pass