from ..settings import get_settings
from . import create_worker

settings = get_settings()
worker = create_worker(settings)
