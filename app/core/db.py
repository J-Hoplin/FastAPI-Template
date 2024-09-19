from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import get_settings

engine = create_engine(str(get_settings().DATABASE_CONNECTION_STRING))
DatabaseSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base class for all models
class BaseModel(DeclarativeBase):
    pass
