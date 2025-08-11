from fastapi import FastAPI
from bill_manager.api.routers import router as api_router

def get_app() -> FastAPI:

    app: FastAPI = FastAPI()
    app.include_router(router=api_router)
    return app