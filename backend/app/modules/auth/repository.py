from datetime import datetime, timedelta, timezone
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import settings
from app.modules.auth.models import RefreshToken, User


class AuthRepository:

    async def get_user_by_email(self, db: AsyncSession, email: str):
        result = await db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def create_user(self,db: AsyncSession,email,full_name,phone_no,password_hash,role_id,) -> User:

        user = User(
            email=email,
            full_name=full_name,
            phone_no=phone_no,
            password_hash=password_hash,
            role_id=role_id,
        )

        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user
    

    async def create_refresh_token(self, db: AsyncSession, user_id: str, refresh_token: str):
        
        refresh_token_entry = RefreshToken(
            user_id=user_id,
            token_hash=refresh_token,
            expires_at = datetime.now(timezone.utc) + timedelta(days=settings.refresh_token_expire_days)
        )

        db.add(refresh_token_entry)
        await db.commit()
        await db.refresh(refresh_token_entry)
        return refresh_token_entry


    async def delete_refresh_token(self, db: AsyncSession):
        pass

Repository = AuthRepository()
