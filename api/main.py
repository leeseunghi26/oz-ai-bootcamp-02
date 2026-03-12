import json
import uuid

from fastapi import FastAPI, Body
from fastapi.responses import StreamingResponse
from redis import asyncio as aredis


redis_client = aredis.from_url("redis://redis:6379", decode_responses=True)

app = FastAPI()

@app.post("/generate")
async def generate_api(user_input: str = Body(...)):
    # job_id 생성
    job_id = str(uuid.uuid4())
    
    # 결과 채널 구독
    channel = f"result:{job_id}"

    pubsub = redis_client.pubsub()
    await pubsub.subscribe(channel)
    print(f"구독 시작: {job_id}")

    # Enqueue(LPUSH)
    job = {"id": job_id, "input": user_input}
    await redis_client.lpush("inference_queue", json.dumps(job))
    print(f"큐에 작업 추가: {job}")

    # 결과를 돌려받아서 응답
    async def event_generator():
        print("Listening 시작...")
        async for message in pubsub.listen():
            if message["type"] != "message":
                continue

            data = message["data"]
            if data == "[DONE]":
                break
            yield data
        
        await pubsub.unsubscribe(channel)
        await pubsub.close()
        print("Listening 종료...")

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )




# from fastapi import FastAPI, Body, Depends
# from sqlalchemy import text
# import redis.asyncio as redis
# from fastapi.responses import StreamingResponse

# # responseS
# redis_client = redis.from_url("redis://redis:6379", decode_responses=True)

# # import time

# # async def coro1():
# #     await time.sleep(3) #양보할 때 await

# from database import SessionFactory


# # 답변 생성을 요청하면, 대기 발생
# # 대기하는 동안, 다른 일 (HTTP 요청)처리
# # llm = Llama( 
# #   model_path=""
# #)

# #llm.create 

# app = FastAPI()
# # [ 쿼리 파라미터(QueryParameter)]
# # GET google.com/search?q=python 

# #GET 새로운 데이터를 만들거나 
# #

# # [1] 사용자가 질문(question)을 요청한다.
# @app.get("/chats")
# async def chat_handler(
#     #REquestBody
#     question: str = Body(..., embed=True), 
#    # Query Parameter
#    #question: str = Query(...),
# ):
#     # [2] 결과 채널을 구독

#     job_id = str(uuid.uuid4()) # 작업을 식별할 수 있는 랜덤 식별자 발급
#     channel = f"result:{job_id}"

#     pubsub = redis_client.pubsub()
#     await pubsub.subscribe(channel)

#     # [3] 답변 생성 작업 Enqueue
    
#     job = {"id": job_id "question": question},
#     await redis_client.lpush("inference_queue", json.dumps(job))
    
#     # [4] 답변 생성 결과를 돌려받기
#     async def event_generator():
#         async for message in pubsub.listen():
#             if message["type"] == "message":
#                 data = message["data"]
#                 if data = message["data"]
#                     break
#                 yield data



#     return StreamingResponse(
#         event_generator(),
#          media_type="text/event-stream",
#     )


# # 1) Path
# # 2) Query
# # 3) Request Body
# #     3-1) xxx: UnicodeTranslateError = Body(...)
# #     3-2) xxx: str = Body


# # @app.get("/users")
# # async def get_users_handler():

# #     with SessionFactory() as session:
# #         stmt = text("SELECT * FROM user ;")
# #         result = session.execute(stmt).mappings().all()
# #     return {"result": result}