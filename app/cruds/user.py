from app import schemas, models
from app.db.config import SessionContext


def get_user(_id: int):
    with SessionContext() as session:
        return session.query(models.User).filter(models.User.id == _id).first()


def find_user_by_username(username):
    with SessionContext() as session:
        return session.query(models.User).filter_by(username=username).first() is not None


def create_user(_in: schemas.UserCreate):
    instance = models.User(
        username=_in.username,
        password=_in.password,
        name=_in.name,
        email=_in.email,
    )
    instance.save()
    return instance
