from app.core.adapters.twilio import TwilioAdapter
from app.settings import Settings


class CallService:
    def __init__(self, settings: Settings, adapter: TwilioAdapter) -> None:
        self._settings = settings
        self._adapter = adapter

    def make_call(self) -> str:
        return self._adapter.create_call(
            self._settings.TWILIO_FROM_NUMBER,
            self._settings.TWILIO_TO_NUMBER,
            self._adapter.build_voice_response(self._settings.DEFAULT_MESSAGE),
        ).sid
