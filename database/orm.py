from datetime import datetime
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(256), nullable=False)
    
    # 1. password_hash는 String 타입으로 수정
    password_hash: Mapped[str] = mapped_column(String(256), nullable=False)
    
    # 2. created_at 오타 수정 및 DateTime 타입으로 정의
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), nullable=False)