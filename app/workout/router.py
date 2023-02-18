from typing import Sequence

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.utils import get_db
from app.workout.schema import Workout, WorkoutCreateModel
from app.workout.view import _get_list, _get_item, _create_item

workout_router = APIRouter(prefix="/workout")


@workout_router.get(path="", status_code=200, response_model=Sequence[Workout])
def get_list(page: int = 1, db: Session = Depends(get_db)):
    return _get_list(db, page)


@workout_router.get(path="/{item_id}", status_code=200, response_model=Workout)
def get_item(item_id: int, db: Session = Depends(get_db)):
    return _get_item(db, item_id)


@workout_router.post(path="", status_code=201, response_model=Workout)
def post_item(workout_in: WorkoutCreateModel, db: Session = Depends(get_db)):
    return _create_item(db, workout_in)
