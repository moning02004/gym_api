from app import schemas, models
from app.db.config import SessionContext


def get_workouts(page: int):
    with SessionContext() as session:
        return session.query(models.Workout).offset((page - 1) * 10).limit(page * 10).all()


def get_workout(_id: int):
    with SessionContext() as session:
        return session.query(models.Workout).filter(models.Workout.id == _id).first()


def create_workout(workout_in: schemas.WorkoutCreateModel):
    instance = models.Workout(
        name=workout_in.name,
        description=workout_in.description,
    )
    instance.save()
    return instance
