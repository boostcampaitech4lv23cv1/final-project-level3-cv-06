from pydantic import BaseModel

class MetaDBOut(BaseModel):
    tag: str
    img_path: str
    class Config:
        orm_mode = True