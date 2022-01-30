from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

from app.settings import Settings


class TwilioAdapter:
    def __init__(self, settings: Settings) -> None:
        self._client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    def create_call(self, caller: str, callee: str, message: str) -> str:
        return self._client.calls.create(
            to=callee, from_=caller, twiml=self._build_voice_response(message)
        ).sid

    def _build_voice_response(self, message: str) -> VoiceResponse:
        response = VoiceResponse()
        response.say(message)
        return response
