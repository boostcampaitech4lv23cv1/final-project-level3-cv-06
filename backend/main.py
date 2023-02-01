import logging
import re

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from api.api_v1 import api_router
from utils import LOGGER

app = FastAPI(
    docs_url='/api/docs',
    redoc_url='/api/redoc',
    openapi_url='/api/openapi.json')

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    x = 'x-forwarded-for'.encode('utf-8')
    response = await call_next(request)
    for header in request.headers.raw:
        if header[0] == x:
            origin_ip, forward_ip = re.split(', ', header[1].decode('utf-8'))
            LOGGER.info(f"origin_ip: {origin_ip}\tforward_ip: {forward_ip}")
    return response


@app.on_event("startup")
async def startup():
    LOGGER.info("Server Start")

@app.on_event("shutdown")
async def shutdown():
    LOGGER.info('Server Down')


app.include_router(api_router, prefix='/api/v1')


