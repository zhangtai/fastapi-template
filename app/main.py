from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api.api_v1.api import api_router

app = FastAPI(title="PROJECT_NAME")


app.include_router(api_router, prefix="/v1")

register_tortoise(
    app,
    db_url="sqlite://:memory:",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
