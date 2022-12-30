from sqlalchemy import create_engine

from db import Base
# from api.models.task import Base

DB_URL = "mysql+asyncmy://root@localhost:3306/demo?charset=utf8"
engine = create_engine(DB_URL, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()