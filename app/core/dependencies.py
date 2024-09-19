from app.core.db import DatabaseSession
from collections.abc import Generator

from sqlalchemy.orm import Session

"""
Declare dependencies for application
"""


# Inject database session
def get_session() -> Generator[Session]:
    db = DatabaseSession()
    try:
        yield db
    finally:
        db.close()
