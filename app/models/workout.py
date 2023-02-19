from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

workout_part = Table("workout_part", Base.metadata,
                     Column("part_id", ForeignKey("part.id"), primary_key=True),
                     Column("workout_id", ForeignKey("workout.id"), primary_key=True))


class Part(Base):
    __tablename__ = "part"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    workouts = relationship("Workout", secondary="workout_part", back_populates="parts")


class Workout(Base):
    __tablename__ = "workout"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.now())

    parts = relationship("Part", secondary="workout_part", back_populates="workouts")
