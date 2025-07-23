from pydantic import BaseModel 
from pydantic.networks import EmailStr
from typing import Optional

class User(BaseModel):
    id: str 
    username: str 
    email: EmailStr
    password: str
    full_name: Optional[str] = None 
    bio: Optional[str] = None 
    role: Optional[str] = None

class UserCreate(User):
    password: str 
    role: str 

class UserResponse(User):
    id: str

class UserCreate(User):
    password: str 
    role: str 

class UserInDB(User):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class UserBase(User):
    role: str