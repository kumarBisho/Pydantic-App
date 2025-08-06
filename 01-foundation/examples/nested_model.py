from pydantic import BaseModel
from typing import Dict, List, Optional

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()  # Necessary for recursive type


address = Address(
    street="Nemua",
    city="Madhubani",
    state="Bihar",
    zip_code="803101"
)

user = User(
    id=1,
    name="Bisho kumar",
    address=address
)

comment = Comment(
    id = 1,
    content="first comment",
    replies= [
        Comment(
            id= 2,
            content="reply1 of first comment",
            replies=None
        ),
        Comment(
            id= 3,
            content="reply2 of first comment",
        )
    ]
)