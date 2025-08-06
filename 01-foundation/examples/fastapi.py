from pydantic import BaseModel, Field, EmailStr
from fastapi import FastAPI, Depends, HTTPException
from typing import List, Optional


app = FastAPI()
class UserSignup(BaseModel):
    username: str
    email: EmailStr
    password: str


class Settings(BaseModel):
    app_name: str = "My FastAPI App v1.0"
    admin_eamil: EmailStr = "admin@chai.com"

def get_settings():
    return Settings()

app.post("/signup")

def signup(user: UserSignup):
    return {"message": f"user {user.username} is signed up successfully!"}


app.get("/settings")
def get_app_settings(settings: Settings = Depends(get_settings)):
    return settings