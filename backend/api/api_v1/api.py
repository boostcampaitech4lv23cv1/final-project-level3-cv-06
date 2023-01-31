from fastapi import APIRouter

from .game import *
from .inference import *
from .meta import *
from .score import *


api_router = APIRouter()

api_router.include_router(game_router, prefix='/game', tags=['game'])
api_router.include_router(infer_router, prefix='/infer', tags=['infer'])
api_router.include_router(db_router, prefix='/meta', tags=['meta'])
api_router.include_router(db_router, prefix='/score', tags=['score'])
