from datetime import datetime

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

from app.db.config import SessionContext

Base = declarative_base()


class Model(Base):
    __bind_key__ = "default"
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.now())

    def save(self):
        with SessionContext() as session:
            session.add(self)
            session.commit()
            session.refresh(self)
