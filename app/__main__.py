from app.settings import get_settings
from app.twilio_adapter import TwilioAdapter

settings = get_settings()
twilio_adapter = TwilioAdapter(settings)

call_sid = twilio_adapter.create_call(
    settings.TWILIO_FROM_NUMBER,
    settings.TWILIO_TO_NUMBER,
    "http://demo.twilio.com/docs/voice.xml",
)

print(call_sid)