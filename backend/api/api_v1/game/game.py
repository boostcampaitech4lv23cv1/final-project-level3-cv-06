from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse, FileResponse


router = APIRouter()


@router.get("/gamestart")
async def gamestart(category: str, mode: str):
    # TODO
    # 카테고리, 모드 따라서 알맞은 사진 반환하기
    
    # predict(category)
    return FileResponse("gif/cat.gif", media_type="image/gif")


@router.post("/gameover")
async def gameover():
    # TODO
    # 점수 받아서 DB에 저장하기
    pass
