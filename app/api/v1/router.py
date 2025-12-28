from fastapi import APIRouter

from app.api.v1.endpoints.health import router as health_router
from app.api.v1.endpoints.companions import router as companions_router
from app.api.v1.endpoints.chat import router as chat_router

router = APIRouter()
router.include_router(health_router)
router.include_router(companions_router, prefix="/companions")
router.include_router(chat_router, prefix="/chat")
