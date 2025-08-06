from pydantic import BaseModel, field_validator, model_validator, computed_field

class User(BaseModel):
    username: str

    @field_validator('username')
    def validate_username(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters long")
        return v
    

class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode = 'after')
    def validate_passwords(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Passwords do not match")
        return values


class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total(self)->float:
        return self.price * self.quantity

