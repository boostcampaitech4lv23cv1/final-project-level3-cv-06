import logging

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
    client_host = request.client.host
    LOGGER.info(f"request by {client_host}")
    response = await call_next(request)
    return response


@app.on_event("startup")
async def startup():
    LOGGER.info("Server Start")

@app.on_event("shutdown")
async def shutdown():
    LOGGER.info('Server Down')


app.include_router(api_router, prefix='/api/v1')


