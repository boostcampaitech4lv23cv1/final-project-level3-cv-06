from typing import Union, List
from pydantic import BaseModel


class GameStart(BaseModel):
    category: str


class GameOver(BaseModel):
    img_paths: List[str]
    score_list: List[int] 
    

class SavePaintOut(BaseModel):
    base_url: str = "https://storage.googleapis.com/image_cloud_demo/"
    label: str
    img_path: str
    class Config:
        orm_mode = True
        

