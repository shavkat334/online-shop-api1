from datetime import datetime
from pydantic import BaseModel, ConfigDict


class WelcomePageResponce(BaseModel):
    message: str


class ProductCreate(BaseModel):
    name: str
    price: float
    amount: int
    discount: float
    picture: str
    expiry_date: datetime


class ProductOut(ProductCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)


class ProductAddToCart(BaseModel):
    product_id: int
    user_id: int
    amount: int


class Order(BaseModel):
    full_name: str
    phone_number: str
    address: str
    user_id: int


class OrderResponce(BaseModel):
    id: int
    full_name: str
    phone_number: str
    address: str
    date_added: datetime
    user_id: int
    status: bool
    model_config = ConfigDict(from_attributes=True)
