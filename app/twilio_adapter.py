from twilio.rest import Client

from app.settings import Settings


class TwilioAdapter:
    def __init__(self, settings: Settings) -> None:
        self._client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    def create_call(self, caller: str, callee: str, message_url: str) -> str:
        return self._client.calls.create(url=message_url, to=callee, from_=caller).sid
