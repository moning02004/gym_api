from fastapi import APIRouter

from app.api.endpoints import workout, user

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(user.router, tags=["User"], prefix="/users")
api_router.include_router(workout.router, tags=["Workout"], prefix="/workouts")
