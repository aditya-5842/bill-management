from fastapi import APIRouter
from bill_manager.api.views.view import router as view_router

router: APIRouter = APIRouter()
router.include_router(view_router)
