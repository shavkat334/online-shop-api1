from fastapi import FastAPI 

from database import engine
from schema import WelcomePageResponce
from models import Base


from admin import admin_routes
from client import client_router

Base.metadata.create_all(bind=engine)


application = FastAPI()

application.include_router(admin_routes)
application.include_router(client_router)


@application.get("/", response_model=WelcomePageResponce)
def welcome_page():
    return {"message":"Welcome to our Online shop "}

