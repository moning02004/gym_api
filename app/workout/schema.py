from pydantic import BaseModel


class Workout(BaseModel):
    id: int
    name: str
    description: str

    # db 데이터를 mapping 하도록 해주는 설정
    class Config:
        orm_mode = True


class WorkoutCreateModel(BaseModel):
    name: str
    description: str
