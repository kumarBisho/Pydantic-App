from pydantic import BaseModel
from typing import List

class Lession(BaseModel):
    lesson_id: int
    lesson_name: str
    content: str
    duration: int  # in minutes

class Module(BaseModel):
    module_id: int
    module_name: str
    description: str
    lessons: List[Lession]

class Course(BaseModel):
    course_id: int
    course_name: str
    instructor: str
    module: List[Module]




