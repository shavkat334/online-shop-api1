from fastapi import APIRouter, Depends
from schema import ProductOut, WelcomePageResponce, ProductAddToCart, Order
from models import Product, CartItem

from sqlalchemy.orm import Session
from database import get_db

client_router = APIRouter()



@client_router.get("/products", response_model=list[ProductOut])
def products(db: Session = Depends(get_db)):
    data = db.query(Product).all()
    return data


@client_router.post("/add-to-cart", response_model=WelcomePageResponce)
def cart_add(product: ProductAddToCart, db: Session = Depends(get_db)):
    new_object = CartItem(**product.model_dump())
    db.add(new_object)
    db.commit()
    return {"message": "Product added to cart successfully!"}


@client_router.get("/mycart")
def products(user_id: int , db: Session = Depends(get_db)):
    data = db.query(CartItem).filter(CartItem.user_id == user_id, CartItem.status == False).all()
    # products = [db.query(Product).filter(Product.id == i.product_id).all() for i in data ]
    return data



@client_router.post("/order", response_model=WelcomePageResponce)
def order(order: Order):
    #1 Order Yaratiladi
    # user_id cart itemlar olinadi va harbiirni order idsi yangi aratilgan orderning id siga tenglanadi
    return {"message":"Order placed successfully !"}