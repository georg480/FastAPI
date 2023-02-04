from random import randint

import fastapi
import uvicorn
from dotenv import find_dotenv, load_dotenv

from costumlogging import logging_config

load_dotenv(find_dotenv())
import os

email = os.getenv("email")
# print(f"email: {email}")
password = os.getenv("email_password")
# print(f'password: {password}')
# def send_mail(to, token, username, email=email, password=password):


def add(a, b):
    return a + b


def devide(a: int, b: int):
    return a / b


print(add(5, 6))

print(devide(8, 2))


def play_random():
    num = randint(0, 10)
    if num > 5:
        return "größer"
    return "kleiner"


class ProductionClass:
    def method(self):
        self.something(1, 2, 3)

    def something(self, a, b, c):
        pass


def printme():
    print("Hallo")


def is_not_flat(data):
    return any(isinstance(i, list) for i in data)


def sum_list(data):
    return sum(data)


from views import home, weather_api

api = fastapi.FastAPI()


def configure():
    api.include_router(home.router)
    api.include_router(weather_api.router)


configure()

if __name__ == "__main__":
    uvicorn.run(api, port=88, log_config=logging_config)


# @app.get("/")
# async def root():
#   return {"message": "Hello World"}


# @app.get("/hello/{name}")
# async def say_hello(name: str):
#   return {"message": f"Hello {name}"}
