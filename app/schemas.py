from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserSignUp(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str

class UserSignIn(BaseModel):
    email: EmailStr
    password: str
    
class VerifyUser(BaseModel):
    email: EmailStr
    code: str
    
class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    
    
class UserResponse(BaseModel):
    id: int
    name: str
    surname: str
    email: EmailStr
    status: bool
    role: str
    created_at: datetime
    class Config:
        from_attributes = True
        
class UserUpdate(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    email: EmailStr

        