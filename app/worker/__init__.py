from pytz import utc

from ..settings import Settings
from .worker import Worker


def create_worker(settings: Settings):
    worker = Worker()
    worker.configure(timezone=utc)

    return worker
