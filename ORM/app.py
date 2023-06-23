from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import desc, func
from database import SessionLocal
from schema import FeedGet, PostGet, UserGet
from table_post import Post
from table_user import User
from table_feed import Feed
from typing import List

app = FastAPI()


@app.get("/post/{id}", response_model=PostGet)
def post_query(id: int = None) -> PostGet:
    result = SessionLocal().query(Post).filter(Post.id == id).one_or_none()
    if result is not None:
        return result
    else:
        raise HTTPException(404, "post not found")


@app.get("/user/{id}", response_model=UserGet)
def user_query(id: int = None) -> UserGet:
    result = SessionLocal().query(User).filter(User.id == id).one_or_none()
    if result is not None:
        return result
    else:
        raise HTTPException(404, "post not found")


@app.get("/user/{id}/feed", response_model=List[FeedGet])
def feed_user(id: int = None, limit: int = 10) -> List[FeedGet]:
    result = SessionLocal().query(Feed).filter(Feed.user_id == id).order_by(desc(Feed.time)).limit(limit).all()
    if result is not None:
        return result
    else:
        raise HTTPException(200, [])


@app.get("/post/{id}/feed", response_model=List[FeedGet])
def feed_post(id: int = None, limit: int = 10) -> List[FeedGet]:
    result = SessionLocal().query(Feed).filter(Feed.post_id == id).order_by(desc(Feed.time)).limit(limit).all()
    if result is not None:
        return result
    else:
        raise HTTPException(200, [])


@app.get("/post/recommendations/", response_model=List[PostGet])
def recommendations_post(id: int = None, limit: int = 10) -> List[PostGet]:
    # result = SessionLocal().query(Feed.post_id, func.count(Feed.post_id))\
    result = SessionLocal().query(Post.id, Post.text, Post.topic).join(Feed) \
        .filter(Feed.action == "like")\
        .group_by(Post.id)\
        .order_by(func.count(Post.id).desc()).limit(limit).all()
    if result is not None:
        return result
    else:
        raise HTTPException(200, [])
