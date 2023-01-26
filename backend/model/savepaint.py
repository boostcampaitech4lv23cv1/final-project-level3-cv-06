from sqlalchemy import Boolean, Column, Integer, String, DateTime
from db import Base

class SavePaint(Base):

    __tablename__ = 'savepaint'

    id = Column(Integer, primary_key=True, index=True)
    created_time = Column(DateTime)
    category = Column(String(100))
    label = Column(String(100))
    img_height = Column(Integer)
    img_width = Column(Integer)
    img_path = Column(String(100))