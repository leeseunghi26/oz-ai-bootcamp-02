from fastapi import FastAPI, Path, Query

app = FastAPI()

def hello_world():
    return {"msg:"hello_world}

#서버에 GET / hello 요청이 들어오면, root_handler를 실행한다
@app.get("/hello")
def root_handler():
    return hello_world()


    #AI 추론

    return {"ping": "pong!!!!!!"}

users = [
    {"id":1, "name": "alex"},
    {"id":2, "name": "bob"},
    {"id":3, "name": "chris"},
]

app = FastAPI()
# 전체 사용자 조회 API 
@app.get("/users")
def get_users_handlers():
    return users

# 1번 사용자 조회 API
# GET /users/1
# GET /users/2

# 1번 사용자 조회 API 
@app.get("/users/1")
def get_first_handlers():
    return users [1]

# {user_id}번 사용자 조회 API
# path(경로) + parameter(매개변수) -> 동작으로 바뀌는 값을 한 번에 처리
# path parameter에 type hint 추가하면 -> 명시한 타입에 맞는지 검사 & 보장
@app.get("/users/{user_id}") #경로여서 
def get_user_handler(
    user_id: int = Path(...,ge=1, description="user_id는 1 이상"), #user_id ...반드시 있어야하는 값이구나, greater than or equal to=ge
    ): # if user (검사하는 코드 필요없음. path가 검사해서 넘겨줌.)

    # gt : 초과
    # ge : 이상
    # lt : 미만
    # le : 이하
    # max_digits: 최대 자리수 000000

    # 1,2,3,4
    # 0,-1,1,2
    # 0 -> chris = users[-1]
    # -2 -> alex = 파이썬에서는 역방향,즉 거꾸로 셈
 
    return users[user_id -1] # 1이상의 숫자로만 나오게 설정할 필요 있음.


# Query Parameter
# google.com/search(path) (커리파라미터: 패스 뒤에 붙어서 키의 벨류 형태로 된 값)-> 데이터 조회시 부가 조건을 명시 ( 필터링, 정렬, 검색, 페이지네이션 등) q=python
# google.com/search?q=python

############### 실습 ##############

# GET / items / {item_name}
# item_name: str & 최대 글자수(max_length) 6
# 응답 형식: {"item_name": ...}
items = [
    {"id": 1, "name": "apple"},
    {"id": 2, "name": "banana"},
    {"id": 3, "name": "cherry"},

@app.get("/items/{item_name}")
def get_item_handler(item_name: str): #안 써도 스트링
 #name 이라는 key
    return {"item_name": item_name}

# 회원가입 API 
# HTTP Method: GET, POST, PUT, PATCH, DELETE
@app.post("/users/sign-up") #regist, sign-up (snake case가 아님)연속되는 이름
def signup_user_handler():
    return {"msg":"hello"}

# 회원 검색 API
@app.get("/users/search?/username")
def search_user_handler():
    return {"msg":"hello"}

# post는 어떤 말은 동사 붙이는 경우가 있다.
# POSToders/1/cancel
# Post / orders /123/cancel -> 주문취소
# Post / auth / login -> 로그인
# Post / payments / 1 / confirm -> 결제 확정


# 1번 댓글 조회 
# GET / comments (명사 복수형 항상)/1(아이디)
# 10번 댓글 삭제
# delete / comments /10
# 새로운 댓글 생성
# post / comments
# comments 집단에 post (id 값을 http로 계좌번호,주민등록번호 등)
# 요청 = HTTP Method(동작, 동사 verb) + URL(대상, 목적어 object)

# 회원가입 API 
# Query Parameter
# ?key=value 형태로 Path 뒤에 붙는 값
# 데이터 조회시 부가 조건을 명시 (필터링, 정렬, 검색, 페이지네이션 등)

@app.get("/users/search?/username")
def search_user_handler(
    name: str = Query(..., min_length=2), 
    #name이라는 key로 넘어오는 Query Parameter 값을 사용하겠다
    return ("name": name)