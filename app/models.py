from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from app.database import Base

Base = declarative_base()
metadata = Base.metadata

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)  # Change the length (255 in this example)
    description = Column(String(255), index=True)
    newtest =  Column(String(255), index=True)
    new_test2 = Column(String(255), index=True)

class Test(Base):
    __tablename__ = "Test"

    id = Column(Integer, primary_key=True, index=True)
    dfgds = Column(String(255), index=True)  # Change the length (255 in this example)
    description = Column(String(255), index=True)
    rqre =  Column(String(255), index=True)
    jhrh = Column(String(255), index=True)