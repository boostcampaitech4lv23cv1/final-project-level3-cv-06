from typing import Union, List
from pydantic import BaseModel


class GameStart(BaseModel):
    category: str


class GameOver(BaseModel):
    category: str
    img_paths: List[str]
    correct_list: List[bool]
    

class SavePaintOut(BaseModel):
    base_url: str = "https://storage.googleapis.com/scraped-img/"
    label: str
    img_path: str
    class Config:
        orm_mode = True
        

