from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)

def encode_token(payload: dict, secret_key: str, algorithm: str) -> dict:
	return jwt.encode(payload, secret_key, algorithm)

def decode_token(token: str, secret_key: str, algorithm: str) -> str:
    try:
        return jwt.decode(token, secret_key, algorithms=[algorithm])
    except Exception as e:
        print(e)
        return None
    
def create_access_token(user_id: int) -> str:
    payload = {
        "sub": user_id,
        "type": "access",
        "exp": datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    }
    return encode_token(payload, settings.SECRET_KEY, settings.ALGORITHM)

def create_refresh_token(user_id: int) -> str:
    payload = {
        "sub": user_id,
        "type": "refresh",
        "exp": datetime.now() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    }
    return encode_token(payload, settings.SECRET_KEY, settings.ALGORITHM)

def check_token_type(payload: dict) -> str:
    if payload["type"] == "access":
        return "access"
    elif payload["type"] == "refresh":
        return "refresh"
    else:
        raise ValueError("Invalid token type")
    
