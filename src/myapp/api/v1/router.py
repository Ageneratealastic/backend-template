# src/myapp/api/v1/router.py
from fastapi import APIRouter
from myapp.api.v1.routes import users, health

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
