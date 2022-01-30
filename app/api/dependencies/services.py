from fastapi import Depends

from app.core.adapters import TwilioAdapter
from app.core.services import CallService
from app.settings import Settings, get_settings


def twilio_adapter(settings: Settings = Depends(get_settings)):
    return TwilioAdapter(settings)


def call_service(
    settings: Settings = Depends(get_settings),
    twilio_adapter: TwilioAdapter = Depends(twilio_adapter),
):
    return CallService(settings, twilio_adapter)
