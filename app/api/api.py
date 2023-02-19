from fastapi import APIRouter

from app.api.endpoints import workout

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(workout.router, tags=["Workout"], prefix="/workouts")
