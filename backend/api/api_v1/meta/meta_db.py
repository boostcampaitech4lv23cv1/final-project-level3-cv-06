from fastapi import APIRouter, HTTPException, Depends, File, UploadFile, BackgroundTasks, Body
from fastapi.responses import StreamingResponse


from sqlalchemy.orm import Session
from typing import List
from io import BytesIO
import pandas as pd
import time

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


@router.post('/create')
async def crawling_data(
    file: UploadFile = File(),
    category: str = Body(),
    db: Session = Depends(get_db),
    bg_task: BackgroundTasks = BackgroundTasks()):
    
    try:
        file_content = await file.read()
        data = pd.read_feather(BytesIO(file_content))
    except Exception as e:
        LOGGER.warning(e)
        return HTTPException(status_code=400, detail="check your extend(you need use feather)")
    
    datas = []
    for idx, row in data.iterrows():
        if category == "animal": # 카테고리 이름 및 테이블 명 통일하기
            # crawling_time = datetime.strptime(row.time, "%Y-%m-%d").date()
            datas.append(
                Animal(
                    created_time=row.crawled_time,
                    tag=row.tag,
                    label=row.label,
                    img_height=row.img_height,
                    img_width=row.img_width,
                    img_path=row.img_path
                )
            )
        elif category == "poster":
            pass
        elif category == "landmark":
            pass
        elif category == "celebrity":
            pass
    db.add_all(datas)
    db.commit()
    LOGGER.debug("add crawling data to DB")
    
    return {"messege": "success"}
    

@router.post('/update')
async def crawling_data(
    file: UploadFile = File(), 
    category: str = Body(),
    db: Session = Depends(get_db)):
    
    try:
        file_content = await file.read()
        data = pd.read_feather(BytesIO(file_content))
    except:
        return HTTPException(status_code=400, detail="check your extend(you need use feather)")
    
    for idx, row in data.iterrows():
        if category == "animal": # 카테고리 이름 및 테이블 명 통일하기
            db_item = db.query(Animal.img_path == row.img_path).first()
            db_item.label = row.label
            db.commit()
        elif category == "poster":
            pass
        elif category == "landmark":
            pass
        elif category == "celebrity":
            pass
        
    return {"messege": "success"}


@router.post('/delete')
async def delete():
    pass