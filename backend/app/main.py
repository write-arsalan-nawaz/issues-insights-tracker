from fastapi import FastAPI
from app.api.routes import auth
from app.api.routes import issues
from app.api.routes import stats
from app.api.api import api_router
from app.workers import aggregator

app = FastAPI()

@app.on_event("startup")
def start_workers():
    aggregator.start()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(issues.router, prefix="/issues", tags=["Issues"])
app.include_router(stats.router, tags=["Stats"])
app.include_router(api_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to the Issues Tracker API"}
