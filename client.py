from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import CartItem, Order as OrderModel, Product
from schema import Order, ProductAddToCart, ProductOut, WelcomePageResponce

client_router = APIRouter()


@client_router.get("/products", response_model=list[ProductOut])
def products(db: Session = Depends(get_db)):
    return db.query(Product).all()


@client_router.post("/add-to-cart", response_model=WelcomePageResponce)
def cart_add(product: ProductAddToCart, db: Session = Depends(get_db)):
    new_object = CartItem(**product.model_dump())
    db.add(new_object)
    db.commit()
    return {"message": "Product added to cart successfully!"}


@client_router.get("/mycart")
def my_cart(user_id: int, db: Session = Depends(get_db)):
    data = (
        db.query(CartItem)
        .filter(CartItem.user_id == user_id, CartItem.status.is_(False))
        .all()
    )
    return data


@client_router.post("/order", response_model=WelcomePageResponce)
def create_order(order_data: Order, db: Session = Depends(get_db)):
    # 1. Yangi Order yaratamiz.
    new_order = OrderModel(
        full_name=order_data.full_name,
        phone_number=order_data.phone_number,
        address=order_data.address,
        user_id=order_data.user_id,
        date_added=datetime.now(),
        status=False,
    )
    db.add(new_order)
    db.flush()  # order.id ni olish uchun

    # 2. Foydalanuvchining hali buyurtma qilinmagan cartlarini topamiz.
    cart_items = (
        db.query(CartItem)
        .filter(
            CartItem.user_id == order_data.user_id,
            CartItem.status.is_(False),
        )
        .all()
    )

    # 3. Har bir cart itemni yangi orderga bog'laymiz.
    for item in cart_items:
        item.order_id = new_order.id
        item.status = True

    db.commit()

    return {"message": "Order placed successfully!"}
