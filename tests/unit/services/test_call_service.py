from unittest.mock import ANY

from pytest import fixture
from twilio.rest.api.v2010.account.call import CallInstance

from app.core.models.call import Call, CallStatus
from app.core.schemas.call import CallCreate
from app.core.services import CallService

call_input = CallCreate(scheduled_to="2022-02-03T00:08:04")


@fixture
def call_instance():
    return Call(id=123, scheduled_to=call_input.scheduled_to)


@fixture
def call_service(settings, twilio_adapter, call_repository, worker):
    return CallService(settings, twilio_adapter, call_repository, worker)


def test_create_call_persists_call(call_service, call_repository):
    call_service.create_call(call_input)

    call_repository.create.assert_called_once_with(call_input.dict())


def test_create_call_schedules_task(
    call_instance, call_service, call_repository, worker
):
    call_repository.create.return_value = call_instance

    call_service.create_call(call_input)

    worker.add_job.assert_called_once_with(
        func=ANY,
        args=[call_instance.id],
        trigger="date",
        run_date=call_instance.scheduled_to,
        id=f"call_{call_instance.id}",
    )


def test_create_call_returns_instance(call_instance, call_service, call_repository):
    call_repository.create.return_value = call_instance

    result = call_service.create_call(call_input)

    assert result == call_instance


def test_make_call_fetches_instance(call_instance, call_service, call_repository):
    call_service.make_call(call_instance.id)

    call_repository.find_by_id.assert_called_once_with(call_instance.id)


def test_make_call_requests_call(
    call_instance, call_service, call_repository, twilio_adapter, settings
):
    call_repository.find_by_id.return_value = call_instance

    call_service.make_call(call_instance.id)

    twilio_adapter.create_call.assert_called_once_with(
        settings.TWILIO_FROM_NUMBER, settings.TWILIO_TO_NUMBER, ANY
    )


def test_make_call_updates_call_instance(
    call_instance, call_service, call_repository, twilio_adapter
):
    call_repository.find_by_id.return_value = call_instance
    twilio_adapter.create_call.return_value = CallInstance(
        version="", payload={"sid": "abc123"}, account_sid=""
    )

    call_service.make_call(call_instance.id)

    assert call_instance.sid == "abc123"
    assert call_instance.status == CallStatus.REQUESTED
    call_repository.save.assert_called_once_with(call_instance, commit=True)
