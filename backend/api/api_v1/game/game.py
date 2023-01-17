from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse, FileResponse, Response, JSONResponse

from utils import get_paint_img, from_image_to_bytes


router = APIRouter()

@router.get('/gamestart')
async def gamestart(category: str, mode: str = "PaintTransformer"):
    # TODO
    # 카테고리, 모드 따라서 알맞은 사진 반환하기
    img_path, answer = get_paint_img(category)
    return FileResponse(path=img_path, headers={"answer" : answer}, media_type='image/jpeg')
    # return JSONResponse(content={"text": 'test'}, media_type="application/json")
    

@router.post('/gameover')
async def gameover():
    # TODO
    # 점수 받아서 DB에 저장하기
    pass