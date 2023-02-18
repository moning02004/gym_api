from datetime import datetime

from sqlalchemy.orm import Session

from app.workout import models
from app.workout.schema import WorkoutCreateModel


def get_workouts(db: Session, page: int):
    return db.query(models.Workout).offset((page - 1) * 10).limit(page * 10).all()


def get_workout(db: Session, _id: int):
    return db.query(models.Workout).filter(models.Workout.id == _id).first()


def create_workout(db: Session, new_model: models.Workout):
    db.add(new_model)
    db.commit()
    db.refresh(new_model)
    return new_model
