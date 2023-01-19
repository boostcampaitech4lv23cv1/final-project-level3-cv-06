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
