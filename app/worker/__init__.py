from functools import lru_cache

from apscheduler.schedulers.background import BackgroundScheduler

from ..settings import Settings, get_settings


def create_worker(settings: Settings):
    worker = BackgroundScheduler()

    return worker


@lru_cache(1)
def get_worker():
    return create_worker(get_settings())
