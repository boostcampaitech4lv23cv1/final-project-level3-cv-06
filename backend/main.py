import logging

from fastapi import FastAPI
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


@app.on_event("startup")
async def startup():
    LOGGER.info("Server Start")

@app.on_event("shutdown")
async def shutdown():
    LOGGER.info('Server Down')


app.include_router(api_router, prefix='/api/v1')


