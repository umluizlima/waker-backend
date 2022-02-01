from pytest import fixture

from app.settings import get_settings


@fixture
def settings():
    return get_settings()
