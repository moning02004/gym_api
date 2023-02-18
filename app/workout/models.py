from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from app.database import Base


class Workout(Base):
    __tablename__ = "workout"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.now())
