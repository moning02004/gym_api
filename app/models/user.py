import bcrypt
from sqlalchemy import Column, String, DateTime, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.base import Model


class User(Model):
    __tablename__ = "user"

    username = Column(String, unique=True)
    password = Column(String)

    email = Column(String)
    name = Column(String)

    profile = relationship("Profile", back_populates="user", uselist=False)

    def encrypt_password(self):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(self.password.encode(), salt)

    def check_password(self, password):
        return bcrypt.checkpw(self.password.encode(), password)


class Profile(Model):
    __tablename__ = "profile"

    user_id = Column(Integer, ForeignKey("user.id"))
    birth_date = Column(Date)

    user = relationship("User", back_populates="profile")
