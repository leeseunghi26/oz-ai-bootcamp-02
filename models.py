#DB를 다루는 모델
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase,Mapped, mapped_column

class Base(DeclarativeBase):
    # ... 변화애 대비하기 위해서 패스 사용/커스텀 할 수 있는 기본 모델 클래스
    pass
# Mapped, mapped_column -> SQLAlchemy
class User(Base):
    __tablename__="user"
# primary_key: 기본키 -> 하나의 데이터를 식별하는 
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(32))

#nullable: null 깂을 허용하는 옵션
age: Mapped[int] = mapped_column(Integer, nullable=True)