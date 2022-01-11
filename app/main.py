from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api.api_v1.api import api_router

app = FastAPI(title="PROJECT_NAME")


app.include_router(api_router, prefix="/v1")


TORTOISE_ORM = {
    "connections": {"default": "sqlite://:memory:"},
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
    "use_tz": True,
}

register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
    add_exception_handlers=True,
)
