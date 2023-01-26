from typing import Union, List

from pydantic import BaseModel

class GameIn(BaseModel):
    category: str
    mode: str = "painttransformer"
    
    
class ImagePath(BaseModel):
    path: str
    

class ImagePaths(BaseModel):
    paths: List[str]
    

class GameOut(BaseModel):
    result_imgs: List[bytes]
    origin_imgs: List[bytes]
    
class SavePaintOut(BaseModel):
    label: List[str]
    img_path: str
    class Config:
        orm_mode = True
        