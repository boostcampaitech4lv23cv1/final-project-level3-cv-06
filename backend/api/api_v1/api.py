from fastapi import APIRouter

from .game import *
from .inference import *

api_router = APIRouter()

api_router.include_router(game_router, prefix="/game", tags=["game"])
api_router.include_router(infer_router, prefix="/infer", tags=["infer"])
