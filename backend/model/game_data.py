from sqlalchemy import Boolean, Column, Integer, String, DateTime
from db import Base

class GameData(Base):

    __tablename__ = 'game_data'

    id = Column(Integer, primary_key=True, index=True)
    created_time = Column(String(20))
    tag = Column(String(300))
    category = Column(String(30))
    label = Column(String(100)) # default = ""
    img_height = Column(Integer)
    img_width = Column(Integer)
    img_path = Column(String(100), nullable=False)
    correct_cnt = Column(Integer, default=0)
    incorrect_cnt = Column(Integer, default=0)
    no_use = Column(Boolean, default=False)
