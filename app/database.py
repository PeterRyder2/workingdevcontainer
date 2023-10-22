from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


db_password = os.environ.get("MYSQL_ROOT_PASSWORD")
SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://root:{db_password}@db/fastapi_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
