from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASES: dict = {
        "default": {
            "url": "postgresql://postgres:postgres@localhost:5432/gym_db",
            "connect_args": {
                "check_same_thread": False,
                "render_as_batch": True
            },
        }
    }


settings = Settings()
