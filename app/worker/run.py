from ..settings import get_settings
from .worker import create_worker

settings = get_settings()
worker = create_worker(settings)
