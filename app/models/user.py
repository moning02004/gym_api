import bcrypt
from sqlalchemy import Column, String, Date, ForeignKey, Integer, DateTime
from sqlalchemy.orm import relationship

from app.models.base import Model


class User(Model):
    __tablename__ = "user"

    username = Column(String, unique=True)
    password = Column(String)

    email = Column(String)
    name = Column(String)

    profile = relationship("Profile", back_populates="user", uselist=False)

    def save(self):
        self.password = bcrypt.hashpw(self.password.encode(), bcrypt.gensalt())
        return super().save()


class Profile(Model):
    __tablename__ = "profile"

    user_id = Column(Integer, ForeignKey("user.id"))
    birth_date = Column(Date)

    user = relationship("User", back_populates="profile")
