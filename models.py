from database import Base

from sqlalchemy import Column, Integer, String, Boolean, Text, Float, DateTime


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    amount = Column(Integer, default=0, nullable=True)
    price = Column(Float, nullable=True,default=0)
    discount = Column(Float, default=0, nullable=True)
    expiry_date = Column(DateTime, nullable=True)
    picture = Column(String, nullable=True)



class CartItem(Base):
    __tablename__ = "cartitems"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    amount = Column(Integer, default=1)
    order_id = Column(Integer, nullable=True)

    status = Column(Boolean, default=False)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    full_name  = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    address = Column(String, nullable=False)
    date_added = Column(DateTime, nullable=False)
    user_id = Column(Integer, nullable=False)

    status = Column(Boolean, default=False)

    
