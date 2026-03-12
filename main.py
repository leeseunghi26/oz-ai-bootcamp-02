from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, Body, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import select
from auth.jwt import create_access_token, verify_access_token, verify_user
from auth.password import hash_password, verify_password
from database.connection import engine, get_session
from database.orm import Base, User,HealthProfile
from request import SignUpRequest, LogInRequest, HealthProfileCreateRequest
from response import UserResponse, LogInResponse, HealthProfileResponse

from routers.user import router as user_router
from routers.prediction import router as prediction_router

@asynccontextmanager
async def lifespan(_):
    #서버 시작 전, 테이블 자동 생성
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(user_router)
app.include_router(prediction_router)
# @app.post(
#     "/users",
#     summary="회원가입 API", 
#     status_code=status.HTTP_201_CREATED,
#     response_model=UserResponse)

# async def signup_handler(
#     body: SignUpRequest = Body(...),
#     session = Depends(get_session),
# ):
    
#     # session.add(...)
#     # await session.commit()

#     # [1] email 중복 검사
#     stmt = select(User).where(User.email == body.email)
#     user = await session.scaler(stmt)

#     if user:
#         raise HTTPException(status_code=409, detail="email already exists")
    
#     # [2] 새로운 유저 데이터 추가 및 비밀번호 해싱 (hashing)
#     new_user = User(
#         email=body.email,
#         password_hash=hash_password(plain_password=body.password),
#     )
#     # pswd1234 -> #103jfdgsdfj! (알아볼 수 없는 걸로 설정)

#     # [3] 데이터 저장
#     session.add(new_user)
#     await session.commit()
#     await session.refresh(new_user) # 데이터베이스에서 id랑 created_at 

#     return new_user
# # xxx
# # Steam, Naver -> 해외 접속 감지 (유출사고 막기)


# @app.post(
#     "/users/login",
#     summary="로그인 API",
#     status_code=status.HTTP_200_OK,
#     response_model=LogInResponse,
# )
# async def login_handler(
#     body: LogInRequest = Body(...),
#     session = Depends(get_session),
# ): 
#     # [1] email 사용자 조회 
#     stmt = select(User).where(User.email == body.email)
#     result = await session.execute(stmt)
#     user: User | None = result.scalar_one_or_none()

#     if not user: 
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="user not found")

#     # [2] body.password & user.password_hash 비교

#     verified = verify_password(plain_password=body.password, password_hash=user.password_hash)
#     if not verified:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="unauthorized")
   
#     # [3] 사용자를 식별할 수 있는 토큰 발급 -> JWT 발급
#     access_token = create_access_token(user_id=user.id)
#     return {"access_token": access_token}

# # 서버로 넘기는 방식 3가지
# # 1. path
# # 2. queryparameter
# # 3. requestbody -> 새로 생성하는 게 아니라
# # 4. header -> 메타데이터 

# # http_bearer = HTTPBearer()

# # @app.get(
# #     "/test",
# # )
# # async def test_handler(
# #     #HTTP Authorlization Header에서 값을 꺼내옴
# #     auth_header: HTTPAuthorizationCredentials = Depends(http_bearer),
# # ):
# #     access_token = auth_header.credentials
# #     payload = verify_access_token(access_token)

# #     user_id = payload["sub"]
# #     return{"payload": payload}


# #프로필 생성
# #프로필 변경
# # 1) 프로필 처음 생성 -> 생성 
# # 2) 프로필 변경 -> 수정 
# @app.post(
#     "/health-profiles",
#     summary="건강 프로필 생성 API",
#     status_code=status.HTTP_201_CREATED,
#     response_model=HealthProfileResponse, 
# )
# async def create_health_profile_handler(
#     user_id: int = Depends (verify_user),
#     body: HealthProfileCreateRequest= Body(...),
#     session = Depends(get_session),
# ):
#     # [1] HealthProfile 중복 검사
#     stmt = select(HealthProfile).where(HealthProfile.user_id == user_id)
#     existing = await session.scalar(stmt)
#     if existing:
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT,
#             detail= "health profile already exists",
#         )

#     # [2] HealthProfile 객체 생성
#     profile_data = body.model_dump()
#     new_profile = HealthProfile(user_id=user_id, **profile_data)
        

#     # [3] DB 저장
#     session.add(new_profile)
#     await session.commit()
#     await session.refresh(new_profile)
#     return new_profile

