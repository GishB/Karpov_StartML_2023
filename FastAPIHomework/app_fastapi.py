# import datetime
from typing import List
from fastapi import FastAPI, HTTPException, Depends
from datetime import date
from datetime import timedelta
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

# from loguru import logger

app = FastAPI()


class User(BaseModel):
    name: str
    surname: str
    age: int
    registration_date: date

    class Config:
        orm_moder = True


# @app.get("/")
# def say_hello():
#     return "hello, world"


@app.get("/")
def sumoftwo(a: int = 0, b: int = 0):
    return a + b


@app.get("/sum_date")
def sumdates(current_date: date, offset: int) -> date:
    result = current_date + timedelta(days=offset)
    # logger.info(result)
    return result


@app.post("/user/validate")
def validate_user(user: User) -> str:
    return f"Will add user: {user.name} {user.surname} with age {user.age}"


# def get_log_data() -> str:
#     """
#     database = data[0]
#     user = data[1]
#     password = data[2]
#     host = data[3]
#     port = data[4]
#     """
#     with open('postgresql_instructions.txt') as f:
#         lines = f.readlines()
#     data = []
#     for i in range(len(lines) - 1):
#         data.append(lines[i].split(',')[0].replace('\n', ''))
#     conn_uri = "postgresql://" + data[0] + ":" + data[1] + "@" + data[2] + ":" + data[3] + "/" + data[4]
#     return conn_uri

def get_db():
    return psycopg2.connect(
        'postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml',
        cursor_factory=RealDictCursor)


# @app.get("/user/{user_id}")
# def get_user_info(user_id: int) -> dict:
#     with get_db().cursor() as cursor:
#         # conn = psycopg2.connect(
#         #     'postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml',
#         #     cursor_factory=RealDictCursor)
#         # cursor = get_db().cursor()
#         cursor.execute(f"""SELECT gender, age, city FROM "user" where id = {user_id}""")
#         result = cursor.fetchone()
#         if not result:
#             raise HTTPException(404, "user not found")
#         else:
#             return result

@app.get("/user/{user_id}")
def get_user_info(db=Depends(get_db), user_id: int = None) -> dict:
    with db.cursor() as cursor:
        # conn = psycopg2.connect(
        #     'postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml',
        #     cursor_factory=RealDictCursor)
        # cursor = get_db().cursor()
        cursor.execute(f"""SELECT gender, age, city FROM "user" where id = {user_id}""")
        result = cursor.fetchone()
        if not result:
            raise HTTPException(404, "user not found")
        else:
            return result


class PostResponse(BaseModel):
    id: int
    text: str
    topic: str

    class Config:
        orm_moder = True


@app.get("/post/{id}", response_model=PostResponse)
def post_query(db=Depends(get_db), id: int = None) -> PostResponse:
    with db.cursor() as cursor:
        cursor.execute(f"""SELECT * FROM post where id = {id}""")
        result = cursor.fetchone()
        if not result:
            raise HTTPException(404, "user not found")
        else:
            return PostResponse(**result)
