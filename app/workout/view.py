from sqlalchemy.orm import Session

from app.workout import crud, models
from app.workout.schema import WorkoutCreateModel


def _get_list(db: Session, page):
    return crud.get_workouts(db, page)


def _get_item(db: Session, _id):
    return crud.get_workout(db, _id)


def _create_item(db: Session, schema: WorkoutCreateModel):
    new_model = models.Workout(
        name=schema.name,
        description=schema.description,
    )
    return crud.create_workout(db, new_model)
