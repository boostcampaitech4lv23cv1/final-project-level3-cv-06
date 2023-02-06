from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

app = FastAPI()

class Inferparam(BaseModel):
    resize_l: int
    K: int
    stroke_num: int # 6, 8, 12 ,16
    mode: str # large or small
    

@app.post("/t1")
async def infer(file: UploadFile = File(...), param: Inferparam = Inferparam(
    resize_l=512,
    K=5,
    stroke_num=8,
    mode="large")):
    return {"test": "test"}