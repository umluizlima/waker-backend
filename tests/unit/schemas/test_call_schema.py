from datetime import datetime

from pydantic.error_wrappers import ValidationError
from pytest import raises

from app.core.models import CallStatus
from app.core.schemas import CallCreate, CallRead

new_call = {
    "scheduled_to": "2022-01-31T00:27:38Z",
}

existing_call = {
    **new_call,
    "id": 123,
    "created_at": datetime.now(),
    "updated_at": datetime.now(),
    "sid": "foeajn12e3",
    "status": CallStatus.WAITING,
}


def test_call_create_requires_only_scheduled_to():
    try:
        CallCreate(**new_call)
    except ValidationError as error:
        assert False, f"'CallCreate(**new_call)' raised an exception {error}"


def test_call_create_must_have_scheduled_to():
    new_call_without_scheduled_to = {**new_call}
    del new_call_without_scheduled_to["scheduled_to"]
    with raises(ValidationError):
        CallCreate(**new_call_without_scheduled_to)


def test_call_read_requires_existing_call():
    try:
        CallRead(**existing_call)
    except ValidationError as error:
        assert False, f"'CallRead(**existing_call)' raised an exception {error}"


def test_call_read_must_have_id():
    call_without_id = {**existing_call}
    del call_without_id["id"]
    with raises(ValidationError):
        CallRead(**call_without_id)


def test_call_read_id_must_be_int():
    broken_id_call = {**existing_call, "id": "abc"}
    with raises(ValidationError):
        CallRead(**broken_id_call)


def test_call_read_must_have_created_at():
    call_without_created_at = {**existing_call}
    del call_without_created_at["created_at"]
    with raises(ValidationError):
        CallRead(**call_without_created_at)


def test_call_read_created_at_must_be_datetime():
    broken_created_at_call = {**existing_call, "created_at": "abc"}
    with raises(ValidationError):
        CallRead(**broken_created_at_call)


def test_call_read_must_have_updated_at():
    call_without_updated_at = {**existing_call}
    del call_without_updated_at["updated_at"]
    with raises(ValidationError):
        CallRead(**call_without_updated_at)


def test_call_read_updated_at_must_be_datetime():
    broken_updated_at_call = {**existing_call, "updated_at": "abc"}
    with raises(ValidationError):
        CallRead(**broken_updated_at_call)


def test_call_read_must_have_status():
    call_without_status = {**existing_call}
    del call_without_status["status"]
    with raises(ValidationError):
        CallRead(**call_without_status)


def test_call_read_status_must_be_enum():
    broken_status_call = {**existing_call, "status": "abc"}
    with raises(ValidationError):
        CallRead(**broken_status_call)


def test_call_read_does_not_require_sid():
    existing_call_without_sid = {**existing_call}
    del existing_call_without_sid["sid"]
    try:
        CallRead(**existing_call_without_sid)
    except ValidationError as error:
        assert (
            False
        ), f"'CallRead(**existing_call_without_sid)' raised an exception {error}"
