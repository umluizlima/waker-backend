from ..settings import get_settings
from . import create_api

settings = get_settings()
api = create_api(settings)
