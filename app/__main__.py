from app.core.adapters import TwilioAdapter
from app.core.services import CallService
from app.settings import get_settings

settings = get_settings()
twilio_adapter = TwilioAdapter(settings)
call_service = CallService(settings, twilio_adapter)

call_sid = call_service.make_call()

print(call_sid)
