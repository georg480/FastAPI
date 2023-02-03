import fastapi
import uvicorn

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
