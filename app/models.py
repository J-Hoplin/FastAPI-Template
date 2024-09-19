from app.core.config import get_settings
from app.core.db import BaseModel, engine, DatabaseSession
from enum import Enum as PyEnum
from sqlalchemy import Column, DateTime, Integer, String, func, Enum, Text
from app.common.util import hash_password, verify_password
from loguru import logger


def initialize_database():
    BaseModel.metadata.create_all(bind=engine)
    session = DatabaseSession()
    settings = get_settings()
    superuser = (
        session.query(User).filter(User.email == settings.SUPERUSER_EMAIL).first()
    )
    if not superuser:
        logger.info("✨Creating superuser")
        hashed_password = hash_password(settings.SUPERUSER_PASSWORD)
        superuser = User(
            first_name="Superuser",
            last_name="Superuser",
            email=settings.SUPERUSER_EMAIL,
            password=hashed_password,
            user_type=UserTypes.SUPERUSER,
        )
        session.add(superuser)
        session.commit()


class UserTypes(PyEnum):
    SUPERUSER = 1
    STAFF = 2
    USER = 3


class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    user_type = Column(Enum(UserTypes), nullable=False, default=UserTypes.USER)
    last_login = Column(DateTime, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def validate_password(self, password: str) -> bool:
        return verify_password(password, self.password)
