from pydantic import BaseModel

class Inferparam(BaseModel):
    resize_l: int
    K: int
    stroke_num: int # 6, 8, 12 ,16
    mode: str # large or small
    