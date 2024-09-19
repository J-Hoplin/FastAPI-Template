from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.main import router
from app.core.middleware import enroll_middlewares
from app.models import initialize_database

app = FastAPI()

# Initialize Database
initialize_database()

# Middlewares(Custom)
enroll_middlewares(app)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
