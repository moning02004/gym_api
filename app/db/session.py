from sqlalchemy.orm import sessionmaker

from app.db.connection import engine

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class SessionContext:
    session = None

    def __enter__(self):
        self.session = Session()
        return self.session

    def __exit__(self, exc_type, exc_value, tb):
        self.session.close()
