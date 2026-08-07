from fastapi import APIRouter, Depends

from schema import WelcomePageResponce, ProductCreate, OrderResponce
from models import Product, Order
from database import get_db
from sqlalchemy.orm import Session


admin_routes  = APIRouter()


@admin_routes.post("/product-create/", response_model=WelcomePageResponce)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    data_new = Product(**product.model_dump())
    db.add(data_new)
    db.commit()
    return {"message":"Product created !"}


@admin_routes.get("/orders/")
def orders(start:int, stop:int, db: Session = Depends(get_db)):
    orders = db.query()
    return orders