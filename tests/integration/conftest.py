from os import environ

from alembic import command
from alembic.config import Config
from pytest import fixture
from testcontainers.postgres import PostgresContainer

from app.core.database import Database
from app.core.models.base import Base
from app.core.repositories import CallRepository
from tests.conftest import get_test_settings


@fixture(scope="session", autouse=True)
def db():
    environ["POSTGRES_DB"] = "waker"
    postgres_container = PostgresContainer("postgres:14.1")
    with postgres_container as postgres:
        environ["DATABASE_URL"] = postgres.get_connection_url()
        database = Database(get_test_settings())
        alembic_cfg = Config("alembic.ini")
        command.upgrade(alembic_cfg, "head")
        yield database


@fixture
def db_session(db: Database):
    with db.get_session() as session:
        try:
            yield session
        finally:
            session.rollback()
            for table in reversed(Base.metadata.sorted_tables):
                session.execute(table.delete())
            session.commit()
            session.close()


@fixture
def call_repository(db_session):
    return CallRepository(db_session)
