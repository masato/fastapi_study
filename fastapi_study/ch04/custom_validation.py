from datetime import date, datetime
from typing import Any, Final
from zoneinfo import ZoneInfo

from pydantic import BaseModel, EmailStr, model_validator, validator

JST: Final = ZoneInfo("Asia/Tokyo")
AGE_120: Final = 120


class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    password_confirmation: str

    @model_validator(mode="before")
    def passwords_match(cls, values: Any) -> Any:  # noqa: ANN401
        password = values.get("password")
        password_confirmation = values.get("password_confirmation")
        if password != password_confirmation:
            msg = "Password dosn't match"
            raise ValueError(msg)
        return values


class Person(BaseModel):
    first_name: str
    last_name: str
    birthdate: date

    @validator("birthdate")
    def valid_birthdate(cls, v: date) -> date:
        delta = datetime.now(tz=JST).date() - v
        age = delta.days / 365
        if age > AGE_120:
            msg = "You seem a bit too old!"
            raise ValueError(msg)
        return v

    def name_dict(self) -> dict:
        return self.model_dump(include={"first_name", "last_name"})
