from fastapi import APIRouter, HTTPException, status

from fastapi_study.ch03.db import db
from fastapi_study.ch03.schemas.post import Post, PostCreate

router = APIRouter()


@router.get("/")
async def all_post() -> list[Post]:
    return list(db.posts.values())


@router.get("/{post_id}")
async def get(post_id: int) -> Post:
    try:
        return db.posts[post_id]
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND) from KeyError


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(post_create: PostCreate) -> Post:
    try:
        db.users[post_create.user]
    except KeyError:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail=f"User with id {post_create.user} doesn't exist.",
        ) from KeyError

    new_id = max(db.posts.keys() or (0,)) + 1
    post = Post(id=new_id, **post_create.model_dump())
    db.posts[new_id] = post
    return post


@router.delete("/post_id", status_code=status.HTTP_204_NO_CONTENT)
async def delete(post_id: int) -> None:
    try:
        db.posts.pop(post_id)
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND) from KeyError
