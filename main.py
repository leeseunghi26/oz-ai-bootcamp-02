from fastapi import FastAPI

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
@app.get("/users/{user_id}")
def get_user_handler(user_id: int):
    return users[user_id -1]