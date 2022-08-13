from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(50))
    age = Column(Integer())
    email = Column(String(100), unique=True)
