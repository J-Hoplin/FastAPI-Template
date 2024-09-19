from app.api.health import controller as health_controller
from app.api.user import controller as user_controller
from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
)
router.include_router(health_controller.router)
router.include_router(user_controller.router)
