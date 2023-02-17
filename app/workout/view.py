from app.workout.mock import WORKOUT_LIST
from app.workout.schema import Workout, WorkoutCreateModel


def _get_list():
    return WORKOUT_LIST


def _get_item(item_id):
    return WORKOUT_LIST[item_id - 1]


def _create_item(schema: WorkoutCreateModel):
    workout = Workout(
        id=len(WORKOUT_LIST) + 1,
        name=schema.name,
        description=schema.description
    )
    WORKOUT_LIST.append(workout.dict())
    return workout

