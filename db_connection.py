#SQLAlchemy에 사용 필요한 기본 설정
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DB 접속 정보(DB 종류, 주소, 포트번호,사용자, 비밀번호, DB 이름)
# sqlite:// -> sqlite를 사용하겠다
#/./test.db -> 현재 프로젝트 경로에 test.db라는 이름의 파일을 만들어라
#sqlite 
DATABASE_URL = "sqlite:///./test.db"

# Engine: 개념 힘을 제공 동작하는 데 있어서 / DB와 연결을 제공하는 객체

engine = create_engine(DATABASE_URL) 

# Session: DB 작업단위
#sessionmaker()의 역할 -> class SessionFactory
#sessionmaker: 클래스르르 만들어주는 함수
#SessionFactory: 세션을 생성하는 클래스
SessionFactory = sessionmaker(
    bind=engine, # 엔진을 연결 

    #기분 옵션
    autocommit=False, # 자동으로 commit() 실행
    autoflush=False, # 자동으로 flush() 실행
    expire_on_commit=False,
)
# sessionmaker()의 역할
# class SessionaFactory(...):
# 세션 인스턴스 셍성
# class SessionFactory(...):

def get_session():
    with SessionFactory() as session:
        yield session