from pydantic import BaseModel
from datetime import datetime

class WelcomePageResponce(BaseModel):
    message : str




class ProductCreate(BaseModel):
    name: str
    price: float
    amount: int
    discount : float
    picture: str
    expiry_date: datetime

class ProductOut(ProductCreate):
    id : int


class ProductAddToCart(BaseModel):
    product_id: int
    user_id : int
    amount: int


class Order(BaseModel):
    full_name : str
    phone_number : str
    address : str
    user_id: int

class OrderResponce(BaseModel):
    pass


