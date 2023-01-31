from sqlalchemy import Boolean, Column, Integer, String, DateTime, Float
from db import Base


class Score(Base):

    __tablename__ = 'score'

    id = Column(Integer, primary_key=True, index=True)
    created_time = Column(String(20))
    user_name = Column(String(30), nullable=False)
    play_time = Column(Float)
    correct_cnt = Column(Integer)
    
    