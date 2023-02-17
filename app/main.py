from fastapi import FastAPI

from app.workout.router import workout_router

app = FastAPI(title="GYM-API")

app.include_router(workout_router)
