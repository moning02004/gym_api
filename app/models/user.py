from datetime import datetime

import bcrypt
from sqlalchemy import Column, Integer, String, DateTime

from app.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)

    email = Column(String)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now())

    def encrypt_password(self):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(self.password.encode(), salt)

    def check_password(self, password):
        return bcrypt.checkpw(self.password.encode(), password)


class Profile(Base):
    __tablename__ = "profile"

    id = Column(Integer, primary_key=True, index=True)
