from app.api.routes import health
from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
)
router.include_router(health.router)