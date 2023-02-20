from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASES: dict = {
        "default": {
            "url": "postgresql://postgres:postgres@localhost:5432/gym_db",
        }
    }


settings = Settings()
