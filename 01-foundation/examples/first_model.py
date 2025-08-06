from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

# Here pydantic will automatically correct the inpur data type into the correct type 
# if it is possible to correct it, otherwise it gives error.
input_data = {'id': '101', 'name': 'Bisho kumar', 'is_active': True}

user= User(**input_data)
print(user)