from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: list[str]
    quantities: Dict[str, int]


class BlogPost(BaseModel):
    title: str
    content: str
    images: Optional[str] = None