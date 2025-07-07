from fastapi import APIRouter
from app.api.routes import issues, auth

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(issues.router, prefix="/issues", tags=["issues"])
