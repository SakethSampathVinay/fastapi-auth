from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from models.models import User
from database import db
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("email")
        if not email:
            raise HTTPException(status_code=401, detail="Token payload missing email")

        user = await db.find_one({"email": email})
        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        return User(
            id=str(user["_id"]),
            username=user["username"],
            email=user["email"],
            password=user["password"],
            full_name=user.get("full_name"),
            bio=user.get("bio"),
            role=user.get("role")
        )
    except JWTError as e:
        raise HTTPException(status_code=401, detail="Invalid token")
