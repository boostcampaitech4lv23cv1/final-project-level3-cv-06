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


@router.get('/read', response_model=List[MetaDBOut])
def read_all_no_label(db: Session = Depends(get_db)):
    no_label_data = read_no_label_and_using(db)
    return no_label_data


@router.post('/duplicate_check')
async def duplicate_check(
    id: str = Body(embed=True),
    category: str = Body(embed=True),
    db: Session = Depends(get_db)):
    """
    meta db에 같은 이미지가 있는지 확인하는 api

    **id**: str(=path)
   
    **category**: str
    
    ---
    
    Return
    
    **valid**: Boolean

    """
    
    valid = True
    datas = read_category(db, category)
    # TODO 리소스 줄이기
    # ordered로 받아 이분탐색 혹은 SQL문으로 한번에 가져오기
    for data in datas:
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
    """
    다른 VM에서 크롤링한 데이터 feather file(data frame)로 받아서 DB에 저장
    
    **file**: format - feather
    
    **category**: str

    """
    
    try:
        file_content = await file.read()
        data = pd.read_feather(BytesIO(file_content))
        create_from_df(db, data, category)
    except Exception as e:
        LOGGER.warning(e)
        return HTTPException(status_code=400, detail="file type error(please check whether file format is feather)")
    
    return {"messege": "success"}
    

@router.post('/update')
async def crawling_update(
    file: UploadFile = File(),
    category: str = Body(),
    db: Session = Depends(get_db)):
    """
    추론 서버에서 label 추론후 DB에 저장
    
    **file**: format - feather
    
    **category**: str
    
    """
    
    try:
        file_content = await file.read()
        data = pd.read_feather(BytesIO(file_content))
    except Exception as e:
        LOGGER.warning(e)
        return HTTPException(status_code=400, detail="file type error(please check whether file format is feather)")
        
    for idx, row in data.iterrows():
        db_item = read_category_and_path(db, row.img_path, category)
        db_item.label = row.label
        db_item.use_status = row.use_status
    db.commit()
        
    return {"messege": "success"}


@router.post('/delete')
async def delete():
    pass