# from bson import ObjectId
from datetime import datetime
from fastapi import APIRouter, HTTPException, status, Depends
from models.models import UserCreate, User, Token
from database import db
from utils import get_password_hash, verify_password, create_access_token

def user_serializer(user) -> dict:
    return {
        'id': str(user['_id']),
        'username': user['username'],
        'email': user['email'],
        'password': user['password'],
        'full_name': user.get('full_name', None),
        'bio': user.get('bio', None)
    }

async def create_user(user: dict):
    user['password'] = get_password_hash(user['password'])
    user['created_at'] = datetime.utcnow()
    result = await db.insert_one(user)
    created_user = await db.find_one({'_id': result.inserted_id})
    return user_serializer(created_user)

async def login_user(email: str, password: str):
    user = await db.find_one({'email': email})
    print(user)
    if user and verify_password(password, user['password']):
        return user_serializer(user)
    return None

