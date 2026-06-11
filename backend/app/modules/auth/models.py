from sqlalchemy import Column, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    # Primary Key
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Basic Information
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    phone_no = Column(String(20), nullable=True)

    # Authentication
    password_hash = Column(String(255), nullable=False)

    # Role Relationship
    role_id = Column(
        BigInteger,
        ForeignKey("roles.id", ondelete="RESTRICT"),
        nullable=False
    )

    # Status
    is_active = Column(Boolean, default=True, nullable=False)

    # Audit Fields
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    # Relationships
    role = relationship("Role", back_populates="users")

    refresh_tokens = relationship(
        "RefreshToken",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    password_reset_tokens = relationship(
        "PasswordResetToken",
        back_populates="user",
        cascade="all, delete-orphan"
    )



class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    # Primary Key
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    # Foreign Key
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    # Store hashed refresh token
    token_hash = Column(
        Text,
        unique=True,
        nullable=False
    )

    # Token Expiry
    expires_at = Column(
        DateTime,
        nullable=False
    )

    # Audit Fields
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    revoked_at = Column(
        DateTime,
        nullable=True
    )

    # Relationship
    user = relationship(
        "User",
        back_populates="refresh_tokens"
    )


class PasswordResetToken(Base):
    __tablename__ = "password_reset_tokens"

    # Primary Key
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    # Foreign Key
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    # Reset Token
    token = Column(
        String(255),
        unique=True,
        nullable=False
    )

    # Token Status
    is_used = Column(
        Boolean,
        default=False,
        nullable=False
    )

    # Audit Fields
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    expires_at = Column(
        DateTime,
        nullable=False
    )

    used_at = Column(
        DateTime,
        nullable=True
    )

    # Relationship
    user = relationship(
        "User",
        back_populates="password_reset_tokens"
    )