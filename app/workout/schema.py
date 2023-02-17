from pydantic import BaseModel


class Workout(BaseModel):
    id: int
    name: str
    description: str


class WorkoutCreateModel(BaseModel):
    name: str
    description: str
