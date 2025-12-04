# src/myapp/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from myapp.api.v1.router import api_router
from myapp.core.config import settings

app = FastAPI(
    title="MyApp API",
    description="A 12-Factor compliant backend service",
    version="0.1.0",
)

# CORS（开发时宽松，生产可限制）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")
