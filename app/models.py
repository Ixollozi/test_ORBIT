from re import S
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,autoincrement=True, primary_key=True)
    
    password = Column(String, nullable=False, max_length=255)
    name = Column(String, nullable=False, max_length=50)
    surname = Column(String, nullable=False, max_length=50)
    email = Column(String, unique=True, index=True, nullable=False, max_length=50)
    status = Column(String, default="no verified")