from sqlalchemy import Boolean, Column, Integer, String, DateTime
from db import Base

class Animal(Base):

    __tablename__ = 'animal'

    id = Column(Integer, primary_key=True, index=True)
    created_time = Column(String(20))
    tag = Column(String(300))
    label = Column(String(100))
    img_height = Column(Integer)
    img_width = Column(Integer)
    img_path = Column(String(100), nullable=False)
    correct_cnt = Column(Integer)
    incorrect_cnt = Column(Integer)
    

class Poster(Base):

    __tablename__ = 'poster'

    id = Column(Integer, primary_key=True, index=True)
    created_time = Column(String(20))
    label = Column(String(100))
    img_height = Column(Integer)
    img_width = Column(Integer)
    img_path = Column(String(100), nullable=False)
    correct_cnt = Column(Integer)
    incorrect_cnt = Column(Integer)
    

class Celebrity(Base):

    __tablename__ = 'celebrity'

    id = Column(Integer, primary_key=True, index=True)
    created_time = Column(String(20))
    label = Column(String(100))
    img_height = Column(Integer)
    img_width = Column(Integer)
    img_path = Column(String(100), nullable=False)
    correct_cnt = Column(Integer)
    incorrect_cnt = Column(Integer)
    
    
class Landmark(Base):

    __tablename__ = 'landmark'

    id = Column(Integer, primary_key=True, index=True)
    created_time = Column(String(20))
    label = Column(String(100))
    img_height = Column(Integer)
    img_width = Column(Integer)
    img_path = Column(String(100), nullable=False)
    correct_cnt = Column(Integer)
    incorrect_cnt = Column(Integer)