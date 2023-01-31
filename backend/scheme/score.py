from typing import Union, List
from pydantic import BaseModel

class ScoreIn(BaseModel):
    user_name: str
    play_time: float
    correct_cnt: int
    
    
class ScoreOut(BaseModel):
    user_name: str
    play_time: float
    correct_cnt: int