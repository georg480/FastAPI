import fastapi
import uvicorn
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
import os

email = os.getenv("email")
# print(f"email: {email}")
password = os.getenv("email_password")
# print(f'password: {password}')
# def send_mail(to, token, username, email=email, password=password):


from views import home, weather_api

api = fastapi.FastAPI()


def configure():
    api.include_router(home.router)
    api.include_router(weather_api.router)


configure()

if __name__ == "__main__":
    uvicorn.run(api, port=88)


# @app.get("/")
# async def root():
#   return {"message": "Hello World"}


# @app.get("/hello/{name}")
# async def say_hello(name: str):
#   return {"message": f"Hello {name}"}
