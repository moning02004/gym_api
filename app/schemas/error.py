from pydantic import BaseModel


class NotFoundSchema(BaseModel):
    message: str