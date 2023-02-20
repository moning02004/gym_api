from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Model


class Part(Model):
    __tablename__ = "part"

    name = Column(String)
    workouts = relationship("Workout", secondary="workout_part", back_populates="parts")


class Workout(Model):
    __tablename__ = "workout"

    name = Column(String)
    description = Column(String)

    parts = relationship("Part", back_populates="workouts")


class PartWorkout(Model):
    __tablename__ = "workout_part"

    part_id = Column(ForeignKey("part.id"), primary_key=True)
    workout_id = Column(ForeignKey("workout.id"), primary_key=True)
