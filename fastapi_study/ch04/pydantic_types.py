from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError


class User(BaseModel):
    email: EmailStr
    website: HttpUrl


try:
    user = User(
        email="jdoe@example.com",
        website=HttpUrl("https://www.example.com"),
    )
    print(user)
except ValidationError as e:
    print(str(e))
