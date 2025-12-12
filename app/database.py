from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config import Settings


settings = Settings()

engine = create_engine(
    url=settings.DATABASE_URL_mysql(),
    echo=True,
    pool_size=5,
    max_overflow=10,
)

SessionLocate = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocate()
    try:
        yield db
    finally:
        db.close()
