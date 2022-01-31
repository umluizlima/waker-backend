from datetime import datetime

from pytest import raises

from app.core.errors import ResourceAlreadyExistsError, ResourceNotFoundError
from app.core.models import Call, CallStatus

new_call = {
    "scheduled_to": "2022-01-31T00:27:38Z",
}
new_call_2 = {"scheduled_to": "2022-11-01T12:14:38Z", "sid": "oiejfojgr13414"}


def test_create_should_return_call_instance(call_repository):
    call = call_repository.create(new_call)
    assert isinstance(call, Call)


def test_create_call_should_have_base_attributes(call_repository):
    call = call_repository.create(new_call)
    assert call.id
    assert isinstance(call.created_at, datetime)
    assert isinstance(call.updated_at, datetime)


def test_create_call_should_have_given_attributes(call_repository):
    call = call_repository.create(new_call)
    assert isinstance(call.scheduled_to, datetime)
    assert call.scheduled_to == datetime.strptime(
        new_call["scheduled_to"], "%Y-%m-%dT%H:%M:%SZ"
    )
    assert call.status == CallStatus.WAITING


def test_create_call_should_be_persisted(call_repository):
    call_repository.create(new_call)
    call_repository.create(new_call_2)
    assert len(call_repository.find_all()) == 2


def test_create_does_not_raise_exception_on_empty_sid(call_repository):
    call_repository.create(new_call)
    call_repository.create(new_call)
    assert len(call_repository.find_all()) == 2


def test_create_raises_exception_on_duplicate_sid(call_repository):
    call_repository.create(new_call_2)
    with raises(ResourceAlreadyExistsError):
        call_repository.create(new_call_2)


def test_find_all_should_return_list(call_repository):
    assert isinstance(call_repository.find_all(), list)


def test_find_all_should_return_existing_calls(call_repository):
    call = call_repository.create(new_call)
    result = call_repository.find_all()
    assert result[0] == call


def test_find_by_id_should_return_call(call_repository):
    call = call_repository.create(new_call)
    result = call_repository.find_by_id(call.id)
    assert result.id == call.id


def test_find_by_id_should_raise_exception_if_not_found(call_repository):
    with raises(ResourceNotFoundError):
        call_repository.find_by_id(123)


def test_find_by_sid_should_return_call(call_repository):
    call = call_repository.create(new_call_2)
    result = call_repository.find_by_sid(call.sid)
    assert result.id == call.id


def test_find_by_sid_should_raise_exception_if_not_found(call_repository):
    with raises(ResourceNotFoundError):
        call_repository.find_by_sid(new_call_2["sid"] + "a")


def test_find_by_sid_should_raise_exception_if_none(call_repository):
    call_repository.create(new_call)
    with raises(ResourceNotFoundError):
        call_repository.find_by_sid(None)


def test_update_by_id_should_update_call(call_repository):
    call = call_repository.create(new_call)
    updated_call = call_repository.update_by_id(call.id, {"sid": "newsid"})
    assert updated_call.sid == "newsid"


def test_update_by_id_should_raise_exception_if_not_found(call_repository):
    with raises(ResourceNotFoundError):
        call_repository.update_by_id(123, {})


def test_update_by_id_should_raise_exception_on_duplicate_entry(call_repository):
    call_1 = call_repository.create(new_call)
    call_2 = call_repository.create(new_call_2)
    with raises(ResourceAlreadyExistsError):
        call_repository.update_by_id(call_1.id, {"sid": call_2.sid})


def test_delete_by_id_should_remove_call(call_repository):
    call = call_repository.create(new_call)
    call_repository.delete_by_id(call.id)
    assert call not in call_repository.find_all()


def test_delete_by_id_should_raise_exception_if_not_found(call_repository):
    with raises(ResourceNotFoundError):
        call_repository.delete_by_id(123)
