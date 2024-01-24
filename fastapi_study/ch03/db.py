from typing import ClassVar

from fastapi_study.ch03.schemas.post import Post
from fastapi_study.ch03.schemas.user import User


class DummyDatabase:
    users: ClassVar[dict[int, User]] = {}
    posts: ClassVar[dict[int, Post]] = {}


db = DummyDatabase()
