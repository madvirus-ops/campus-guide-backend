import os

from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
import pytz


load_dotenv()
# Retrieve the database URL from the environment variables
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")


# Create the SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=10,
    max_overflow=20, 
    pool_timeout=30,  
    pool_recycle=1800, 
    pool_pre_ping=True
)



def get_session():
    with Session(engine) as session:
        yield session


def create_session():
    return Session(engine)




# SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


TZ = pytz.timezone("Africa/Lagos")

tz = TZ


def get_env(value: str):
    return os.getenv(value)
