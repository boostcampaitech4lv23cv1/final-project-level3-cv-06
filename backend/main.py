# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from api.api_v1 import api_router


app = FastAPI(
    docs_url="/api/docs", redoc_url="/api/redoc", openapi_url="/api/openapi.json"
)

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

app.include_router(api_router, prefix="/api/v1")
