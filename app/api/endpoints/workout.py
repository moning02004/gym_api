from typing import Sequence

from fastapi import APIRouter

from app import schemas, cruds

router = APIRouter()


@router.get(path="", status_code=200, response_model=Sequence[schemas.Workout])
def get_list(page: int = 1):
    return cruds.get_workouts(page)


@router.get(path="/{item_id}", status_code=200, response_model=schemas.Workout)
def get_item(item_id: int):
    return cruds.get_workout(item_id)


@router.post(path="", status_code=201, response_model=schemas.Workout)
def post_item(workout_in: schemas.WorkoutCreateModel):
    return cruds.create_workout(workout_in)
