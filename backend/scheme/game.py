from typing import Union, List
from pydantic import BaseModel


class GameStart(BaseModel):
    category: str


class GameOver(BaseModel):
    img_paths: List[str]
    socore_list: List[int] 
    

class SavePaintOut(BaseModel):
    label: str
    img_path: str
    class Config:
        orm_mode = True
        

