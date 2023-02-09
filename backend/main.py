import logging
import re

from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from api.api_v1 import api_router
from utils import LOGGER

app = FastAPI(
    docs_url="/api/docs", redoc_url="/api/redoc", openapi_url="/api/openapi.json"
)

origins = [
    "*",
]

black_list = [
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def check_ip(request: Request, call_next):
    """
    사용자 IP 체크\n
    접근한 URL, METHOD 체크
    """
    # ip_addr = request.headers.get("X-Forwarded-For")
    ip_addr = request.headers.get('X-Real-IP')
    
    if ip_addr in black_list:
        data = {
            'message': f'IP {ip_addr} is not allowed to access this resource.'
        }
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=data)
    
    LOGGER.info(f"request addr: {ip_addr}, url: {request.url}, method: {request.method}")
    response = await call_next(request)
    return response


@app.on_event("startup")
async def startup():
    """
    서버 시작시 수행
    """
    LOGGER.info("Server Start")


@app.on_event("shutdown")
async def shutdown():
    """
    서버 다운시 수행
    """
    LOGGER.info('Server Down')


app.include_router(api_router, prefix='/api/v1')


