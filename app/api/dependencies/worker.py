from fastapi import Depends

from app.settings import Settings, get_settings
from app.worker import get_worker


def worker(settings: Settings = Depends(get_settings)):
    return get_worker(settings)
