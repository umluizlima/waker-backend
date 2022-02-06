from pytest import fixture
from starlette.testclient import TestClient

from app.api import create_api
from app.settings import get_settings


@fixture
def client(settings):
    api = create_api(settings)
    api.dependency_overrides[get_settings] = lambda: settings
    client = TestClient(api)
    return client
