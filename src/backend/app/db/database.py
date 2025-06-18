from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os
from contextlib import contextmanager
from sqlalchemy.engine import URL

load_dotenv()

url = URL.create(
    drivername="postgresql",
    username=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD'),
    host=os.getenv('POSTGRES_HOST'),
    port=5432,
    database=os.getenv('POSTGRES_DB')
)

engine = create_engine(url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@contextmanager
def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
