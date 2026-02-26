from fastapi import FastAPI, Path, Query, status, HTTPException, Depends
from sqlalchemy import select

from db_connection import SessionFactory, get_session
from schema import UserSignUpRequest, UserSignUpResponse, UserResponse 
from models import User

app = FastAPI()

def hello_world():
    return {"msg:"}

# 서버에 GET / hello 요청이 들어오면, root_handler를 실행한다
@app.get("/hello")
def root_handler():
    return hello_world()

# 더미 데이터
users = [
    {"id":1, "name": "alex", "age": 20},
    {"id":2, "name": "bob", "age": 30},
    {"id":3, "name": "chris", "age": 40},
]

# 전체 사용자 조회 API 
@app.get(
    "/users",
    status_code=status.HTTP_200_OK,
    response_model=list[UserResponse],
)
def get_users_handlers():
    with SessionFactory() as session:
        # statement = 구문 -> SELECT * FROM user
        stmt = select(User)
        result = session.execute(stmt)
        users_db = result.scalars().all()
    return users_db

# 1번 사용자 조회 API 
@app.get("/users/1")
def get_first_handlers():
    return users[1]

# {user_id}번 사용자 조회 API
@app.get("/users/{user_id}") 
def get_user_handler(
    user_id: int = Path(..., ge=1, description="사용자의 ID"),
    field: str = Query(None, description="출력할 필드 선택(id 또는 name)"),
):
    # 에러 처리 로직 들여쓰기 정렬
    if user_id > len(users):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 사용자의 ID입니다."
        )
    
    user = users[user_id - 1]

    if field in ("id", "name"):
        return {field: user[field]}
    return user

# 아이템 조회 API
@app.get("/items/{item_name}")
def get_item_handler(item_name: str):
    return {"item_name": item_name}

# 회원 검색 API
@app.get("/users/search")
def search_user_handler(
    name: str = Query(..., min_length=2), 
    age: int = Query(None, ge=1),
):
    return {"name": name}

# 회원가입 API
@app.post(
    "/users/sign-up",
    status_code=status.HTTP_201_CREATED,
    response_model=UserSignUpResponse,
)
def sign_up_handler(body: UserSignUpRequest):
    # 인스턴스 생성 및 세션 작업 들여쓰기 정렬
    new_user = User(name=body.name, age=body.age)
    
    with SessionFactory() as session:
        session.add(new_user)
        session.commit()
        session.refresh(new_user) # 저장된 데이터를 다시 읽어옴
    
    return new_user

# 사용자 삭제(회원탈퇴) API
@app.delete(
    "/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user_handler(user_id: int = Path(..., ge=1)):
    if user_id > len(users):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="존재하지 않는 사용자의 ID입니다."
        )
    user = users[user_id - 1]
    users.remove(user)
    return None