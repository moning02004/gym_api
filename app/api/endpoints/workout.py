from typing import Sequence

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import models, schemas, cruds
from app.schemas import Workout, WorkoutCreateModel
from app.utils import get_db

router = APIRouter()


@router.get(path="", status_code=200, response_model=Sequence[Workout])
def get_list(page: int = 1, db: Session = Depends(get_db)):
    return cruds.get_workouts(db, page)


@router.get(path="/{item_id}", status_code=200, response_model=Workout)
def get_item(item_id: int, db: Session = Depends(get_db)):
    return cruds.get_workout(db, item_id)


@router.post(path="", status_code=201, response_model=schemas.Workout)
def post_item(workout_in: WorkoutCreateModel, db: Session = Depends(get_db)):
    new_model = models.Workout(
        name=workout_in.name,
        description=workout_in.description,
    )
    return cruds.create_workout(db, new_model)
