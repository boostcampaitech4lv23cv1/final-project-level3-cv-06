from sqlalchemy import Boolean, Column, Integer, String, DateTime
from db import Base

from fastapi import UploadFile, File

class Crawling(Base):
    file: UploadFile = File(),
    category: str