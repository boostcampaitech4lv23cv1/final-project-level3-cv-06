from fastapi import APIRouter, HTTPException, Depends, File, UploadFile
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
async def crawling_data(file: UploadFile = File(), db: Session = Depends(get_db)):
    # TODO
    # feather 확장자 받아서 db에 넣기
    extend = file.filename.split('.')[-1]
    if extend == "feather":
        file_content = await file.read()
        data = pd.read_feather(BytesIO(file_content))
    elif extend == "csv":
        file_content = await file.read()
        data = pd.read_csv(BytesIO(file_content), encoding="utf-8")
    else:
        return {"error": "feather or csv file이 아닙니다"}
    
    datas = []
    for idx, row in data.iterrows():
        if row.category == "animal": # 카테고리 이름 및 테이블 명 통일하기
            # crawling_time = datetime.strptime(row.time, "%Y-%m-%d").date()
            datas.append(
                Animal(
                    created_time=row.time,
                    tag=row.tag,
                    label=row.label,
                    img_height=row.img_height,
                    img_width=row.img_width,
                    img_path=row.img_path
                )
            )
        elif row.category == "landmark":
            pass
        elif row.category == "celebrity":
            pass
    db.add_all(datas)
    db.commit()
    
    return {"messege": "success"}
    


@router.post('/update')
async def crawling_data(file: UploadFile = File(), db: Session = Depends(get_db)):
    extend = file.filename.split('.')[-1]
    if extend == "feather":
        file_content = await file.read()
        data = pd.read_feather(BytesIO(file_content))
    elif extend == "csv":
        file_content = await file.read()
        data = pd.read_csv(BytesIO(file_content), encoding="utf-8")
    else:
        return {"error": "feather or csv file이 아닙니다"}
    
    for idx, row in data.iterrows():
        if row.category == "animal": # 카테고리 이름 및 테이블 명 통일하기
            db_item = db.query(Animal.img_path == row.img_path).first()
            db_item.label = row.label
            db.commit()
        elif row.category == "landmark":
            pass
        elif row.category == "celebrity":
            pass
        
    return {"messege": "success"}