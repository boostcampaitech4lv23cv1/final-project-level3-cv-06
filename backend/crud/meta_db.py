from sqlalchemy.orm import Session
from sqlalchemy import and_
from fastapi import HTTPException


from utils import LOGGER
from model import *
from scheme import *

def read_no_label_and_using(db: Session):
    return db.query(GameData).filter(and_(GameData.label == "", GameData.use_status == True)).all()

