from fastapi import APIRouter

from .game import game_router
from .meta import db_router
from .score import score_router


api_router = APIRouter()

api_router.include_router(game_router, prefix='/game', tags=['game'])
api_router.include_router(db_router, prefix='/meta', tags=['meta'])
api_router.include_router(score_router, prefix='/score', tags=['score'])
