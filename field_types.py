from datetime import datetime
from typing import Final
from zoneinfo import ZoneInfo

from pydantic import ValidationError

from fastapi_study.ch04.schemas import Address, Gender, Person

JST: Final = ZoneInfo("Asia/Tokyo")


try:
    person = Person(
        first_name="John",
        last_name="Doe",
        age=40,
        gender=Gender.MALE,
        birthdate=datetime(1999, 12, 1, tzinfo=JST),
        interests=["travel", "sports"],
        address=Address(
            street_address="12 Squirell Street",
            postal_code="424242",
            city="Woodtown",
            country="US",
        ),
    )

    print(person)

except ValidationError as e:
    print(str(e))
