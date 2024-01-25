from typing import ClassVar

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str


class PostPartialUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


class PostCreate(PostBase):
    pass


class PostRead(PostBase):
    id: int


class Post(PostBase):
    id: int
    nb_views: int = 0


class DummyDatabase:
    posts: ClassVar[dict[int, Post]] = {}


db = DummyDatabase()

app = FastAPI()


@app.patch("/posts/{post_id}", response_model=PostRead)
async def partial_update(post_id: int, post_update: PostPartialUpdate) -> Post:
    try:
        post_db = db.posts[post_id]

        updated_fields = post_update.model_dump(exclude_unset=True)
        updated_post = post_db.model_copy(update=updated_fields)

        db.posts[post_id] = updated_post
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND) from KeyError
    else:
        return updated_post
