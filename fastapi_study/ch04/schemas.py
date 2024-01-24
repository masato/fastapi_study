from datetime import date
from enum import StrEnum

from pydantic import BaseModel, Field


class UserProfile(BaseModel):
    nickname: str
    location: str | None = None
    subscribed_newsletter: bool = True


class Gender(StrEnum):
    MALE = "male"
    FEMALE = "female"
    NON_BINARY = "non_binary"


class Address(BaseModel):
    street_address: str
    postal_code: str
    city: str
    country: str


class Person(BaseModel):
    first_name: str = Field(..., min_length=3)
    last_name: str = Field(..., min_length=3)
    age: int | None = Field(None, ge=0, le=120)
    gender: Gender
    birthdate: date
    interests: list[str]
    address: Address
