from sqlalchemy import create_engine
from sqlalchemy import sessionmaker, declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql://user:1234@localhost:5432/crm_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocate = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base