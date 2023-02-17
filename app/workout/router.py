from typing import Sequence

from fastapi import APIRouter

from app.workout.schema import Workout, WorkoutCreateModel
from app.workout.view import _get_list, _get_item, _create_item

workout_router = APIRouter(prefix="/workout")


@workout_router.get(path="", status_code=200, response_model=Sequence[Workout])
def get_list():
    return _get_list()


@workout_router.get(path="/{item_id}", status_code=200, response_model=Workout)
def get_item(item_id: int):
    return _get_item(item_id)


@workout_router.post(path="", status_code=201, response_model=Workout)
def post_item(workout_in: WorkoutCreateModel):
    return _create_item(workout_in)
