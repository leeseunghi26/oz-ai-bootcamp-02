from pydantic import BaseModel


# 회원가입 요청 본문(Request Body) 의 데이터 형태
class UserSignUpRequest(BaseModel):
    name: str #필수값(required)
    age: int | None = None


# 회원가입 응답 본문(Response Body)의 데이터 형태
class UserResponse(BaseModel):
    id: int
    name: str #필수값(required)
    age: int | None = None
class UserSignUpResponse(BaseModel):
    id: int
    name: str #필수값(required)
    age: int | None = None
class UserUpdateRequest(BaseModel):
    name: str | None = None
    age: int | None = None
    
#1) 서버에서 원하는 데이터 형식으로 응답이 반환되는지 검증
#2) 노출되면 안 되는 값을 자동으로 제거
#3) API 문서에 예상되는 응답 출력
