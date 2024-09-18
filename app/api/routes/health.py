from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/health",
    tags=["health"],
)

@router.get("/ping")
def server_ping():
    return JSONResponse(content={"result": "pong"},status_code=200)