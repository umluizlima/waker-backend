from app.core.adapters.twilio import TwilioAdapter
from app.core.models.call import Call
from app.core.repositories import CallRepository
from app.core.schemas.call import CallCreate
from app.settings import Settings


class CallService:
    def __init__(
        self, settings: Settings, adapter: TwilioAdapter, repository: CallRepository
    ) -> None:
        self._settings = settings
        self._adapter = adapter
        self._repository = repository

    def make_call(self) -> str:
        return self._adapter.create_call(
            self._settings.TWILIO_FROM_NUMBER,
            self._settings.TWILIO_TO_NUMBER,
            self._adapter.build_voice_response(self._settings.DEFAULT_MESSAGE),
        ).sid

    def create_call(self, call: CallCreate) -> Call:
        return self._repository.create(call.dict())
