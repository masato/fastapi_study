from fastapi import APIRouter, HTTPException, status

from fastapi_study.ch03.db import db
from fastapi_study.ch03.schemas.user import User, UserCreate

router = APIRouter()


@router.get("/")
async def all_users() -> list[User]:
    return list(db.users.values())


@router.get("/{user_id}")
async def get(user_id: int) -> User:
    try:
        return db.users[user_id]
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND) from KeyError


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create(user_create: UserCreate) -> User:
    new_id = max(db.users.keys() or (0,)) + 1
    user = User(id=new_id, **user_create.dict())
    db.users[new_id] = user
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(user_id: int) -> None:
    try:
        db.users.pop(user_id)
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND) from KeyError
