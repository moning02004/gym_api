from fastapi import FastAPI

from app import workout
from app.database import engine
from app.workout.router import workout_router

app = FastAPI(title="GYM-API")


app.include_router(workout_router)
workout.models.Base.metadata.create_all(bind=engine)
