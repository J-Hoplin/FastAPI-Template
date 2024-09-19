from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/health",
    tags=["health"],
)


@router.get("/")
def server_ping():
    return JSONResponse(content={"result": "OK"}, status_code=200)
