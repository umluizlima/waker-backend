from twilio.rest import Client
from twilio.rest.api.v2010.account.call import CallInstance
from twilio.twiml.voice_response import VoiceResponse

from app.settings import Settings


class TwilioAdapter:
    def __init__(self, settings: Settings, client: Client | None = None) -> None:
        self._client = client or Client(
            settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN
        )

    def create_call(
        self, caller: str, callee: str, response: VoiceResponse
    ) -> CallInstance:
        return self._client.calls.create(to=callee, from_=caller, twiml=response)

    def build_voice_response(self, message: str) -> VoiceResponse:
        response = VoiceResponse()
        response.say(message)
        return response
