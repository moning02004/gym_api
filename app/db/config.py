from sqlalchemy import create_engine

from app.core.settings import settings

from sqlalchemy.orm import sessionmaker

engine = create_engine(**settings.DATABASES["default"])

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class SessionContext:
    session = None

    def __enter__(self):
        self.session = Session()
        return self.session

    def __exit__(self, exc_type, exc_value, tb):
        self.session.close()
