from pydantic import BaseModel

# todo: create product model with id, name, price and in_stock

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True