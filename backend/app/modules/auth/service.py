from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.modules.auth.repository import Repository
from app.modules.auth.schemas import RegisterRequest , LoginRequest
from app.modules.auth.Password_hash import hash_password , verify_password
from app.modules.auth.jwt_helper import create_access_token, create_refresh_token


class AuthService:

    async def register_user_service(self, data: RegisterRequest, db: AsyncSession):

        existing_user = await Repository.get_user_by_email(db, data.email)

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="User with this email already exists",
            )

        password_hash = hash_password(data.password)

        return await Repository.create_user(
            db,
            email=data.email,
            full_name=data.full_name,
            phone_no=data.phone_no,
            password_hash=password_hash,
            role_id=2,
        )
    

    async def login_user_service(self, data: LoginRequest, db: AsyncSession):
        
        user = await Repository.get_user_by_email(db, data.email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )

        if not verify_password(data.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )
        
         # Generate tokens
        access_token = create_access_token(user)
        refresh_token = create_refresh_token(user)

        hashed_refresh_token = hash_password(refresh_token)

        # Store refresh token in database
        await Repository.create_refresh_token(db, user.id, hashed_refresh_token)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }


    async def logout_user_service(self, db: AsyncSession):
        
        await Repository.delete_refresh_token(db)
        return {"message": "Successfully logged out"}

Service = AuthService()
