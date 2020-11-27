from fastapi import APIRouter
from api.endpoints import h3

api_router = APIRouter()

api_router.include_router(h3.router, prefix="/h3", tags=["h3"])
