from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    address: Address
    created_at: datetime = Field(default=datetime.now())
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders= {
            datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')
        }
    )


# create user

user = User(
    id=1,
    name="John Doe",
    email="WYVdK@example.com",
    address = Address(
        street="123 Main St",
        city="Springfield",
        zip_code="12345"
    ),
    tags=["premium", "vip"],
    created_at= datetime(2023, 10, 1, 12, 34, 56, 786543)
)

# using model_dump to serialize the user object, -> its output is a dictionary

python_dict = user.model_dump()
print(python_dict)

print("---------------\n")
# using model_dump_json to serialize the user object to JSON

json_string = user.model_dump_json()
print(json_string)