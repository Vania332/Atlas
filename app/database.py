from sqlalchemy import create_engine
from sqlalchemy import sessionmaker, declarative_base
from config import Settings

engine = create_engine(
    url=Settings.DATABASE_URL_pcycopg,
    echo=True,
    pool_size=5,
    max_overflow=10,
    )

SessionLocate = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base