from typing import Union

from pydantic import BaseModel

class GameIn(BaseModel):
    category: str
    mode: str = "PaintTransformer"