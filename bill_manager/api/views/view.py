# add code with fastapi endpoint with health check returning "OK"
from fastapi import APIRouter

router: APIRouter = APIRouter()


@router.get("/health")
async def health_check():
    return {"status": "OK"}