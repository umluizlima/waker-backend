from pytest import fixture
from starlette.status import (
    HTTP_201_CREATED,
    HTTP_405_METHOD_NOT_ALLOWED,
    HTTP_422_UNPROCESSABLE_ENTITY,
)

from app.core.errors import ResourceNotFoundError
from app.core.schemas import CallRead

call_dict_1 = {"scheduled_to": "2022-01-06T12:04:00Z"}
call_dict_2 = {}


def create_call_request(client, payload):
    return client.post(
        "/api/v1/calls",
        json=payload,
    )


@fixture
def create_call_response(client, call_repository):
    yield create_call_request(client, call_dict_1)
    for call in call_repository.find_all():
        call_repository.delete_by_id(call.id)


def test_create_call_should_return_status_201(create_call_response):
    assert create_call_response.status_code == HTTP_201_CREATED


def test_create_call_endpoint_should_accept_post(create_call_response):
    assert create_call_response.status_code != HTTP_405_METHOD_NOT_ALLOWED


def test_create_user_should_have_valid_payload(client):
    response = create_call_request(client, call_dict_2)
    assert response.status_code == HTTP_422_UNPROCESSABLE_ENTITY


def test_create_call_should_return_call_schema(create_call_response):
    assert CallRead(**create_call_response.json())


def test_create_call_should_persist_to_database(create_call_response, call_repository):
    try:
        call_repository.find_by_id(create_call_response.json()["id"])
    except ResourceNotFoundError as error:
        assert False, f"Call was not persisted to database {error}"
