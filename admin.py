from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Order, Product
from schema import OrderResponce, ProductCreate, WelcomePageResponce

admin_routes = APIRouter()


@admin_routes.post("/product-create/", response_model=WelcomePageResponce)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    data_new = Product(**product.model_dump())
    db.add(data_new)
    db.commit()
    return {"message": "Product created !"}


@admin_routes.get("/orders/", response_model=list[OrderResponce])
def orders(start: int = 0, stop: int = 10, db: Session = Depends(get_db)):
    if start < 0:
        start = 0
    if stop <= start:
        stop = start + 10

    data = (
        db.query(Order)
        .order_by(Order.id.desc())
        .offset(start)
        .limit(stop - start)
        .all()
    )
    return data
