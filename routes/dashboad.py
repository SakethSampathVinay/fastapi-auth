from fastapi import FastAPI, Depends, HTTPException, APIRouter
from models.models import User, UserCreate, UserResponse, UserBase, Token
from services.services import create_user, login_user
from dependencies import get_current_user
from utils import create_access_token

router = APIRouter()

@router.get('/profile')
def get_profile(current_user: User = Depends(get_current_user)):
    return {'message': f"Welcome {current_user.full_name}!"}

@router.get('/admin')
def admin_route(current_user: User = Depends(get_current_user)):
    if current_user.role != 'admin':
        raise HTTPException(status_code = 403, details = "Admins only!")
    return {'message': "Welcome Admin!"}