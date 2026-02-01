from sqlalchemy import Column, Integer, String, DateTime, Boolean
from app.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,autoincrement=True, primary_key=True)
    
    password = Column(String, nullable=False, max_length=255)
    name = Column(String, nullable=False, max_length=50)
    surname = Column(String, nullable=False, max_length=50)
    email = Column(String, unique=True, index=True, nullable=False, max_length=50)
    status = Column(Boolean, default=False)
    role = Column(String, default="user")
    created_at = Column(DateTime, default=datetime.now)
    code = Column(String, nullable=True, max_length=6)