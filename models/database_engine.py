from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy import inspect
from models.github_model import (
    PullRequest,
)
DATABASE_URL = ("postgresql://postgres:529440100@localhost/fast_db")
engine = create_engine(DATABASE_URL)

SessionLocal = lambda: Session(engine)


def check_table_exists(table_name: str) -> bool:
    inspector = inspect(engine)
    return table_name in inspector.get_table_names()


def init_db():
    if not check_table_exists("pullrequest"):
        print("Table 'pullrequest' does not exist. Creating the table...")
        SQLModel.metadata.create_all(
            bind=engine, tables=[PullRequest.__table__]
        )
    else:
        print("Table 'pullrequest' already exists.")


init_db()
