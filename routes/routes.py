from fastapi import FastAPI, Depends, HTTPException, APIRouter
from models.models import User, UserCreate, UserResponse, UserBase, Token
from services.services import create_user, login_user
from dependencies import get_current_user
from utils import create_access_token

router = APIRouter()

@router.post('/register', response_model = UserResponse)
async def register_user(user: UserCreate):
    user_dict = user.dict()
    created_user = await create_user(user_dict)
    return created_user

@router.post('/login', response_model = Token)
async def login(email: str, password:str):
    user = await login_user(email, password)
    if user:
        access_token = create_access_token({'email': user['email']})
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code = 401, detail = "Invalid crendentials")