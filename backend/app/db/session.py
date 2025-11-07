"""Session factory for database interactions."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


engine = create_engine(settings.database_url, echo=settings.dev_mode)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
  """Yield a database session for dependency injection."""

  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

