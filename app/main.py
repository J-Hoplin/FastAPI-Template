from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.main import router
from app.core.middleware import enroll_middlewares
app = FastAPI()
enroll_middlewares(app)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)