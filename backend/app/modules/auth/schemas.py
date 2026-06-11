from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional
from datetime import datetime
import uuid



class RegisterRequest(BaseModel):
    email: EmailStr
    full_name: str = Field(..., max_length=255)
    phone_no: Optional[str] = Field(None, max_length=20)
    password: str = Field(..., min_length=8, max_length=128)
    confirm_password: str

    @validator("confirm_password")
    def passwords_match(cls, v, values):
        if "password" in values and v != values["password"]:
            raise ValueError("Passwords do not match")
        return v

    @validator("password")
    def password_strength(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one digit")
        return v
    

class RegisterResponse(BaseModel):
    id: uuid.UUID
    email: str
    full_name: str
    phone_no: Optional[str]
    is_active: bool
    created_at: datetime


class UserResponse(BaseModel):
    id: uuid.UUID
    email: str
    full_name: str
    phone_no: Optional[str]
    role_id: int

    is_active: bool

    created_at: datetime
    updated_at: datetime


class LoginRequest(BaseModel):
    email: EmailStr
    password: str