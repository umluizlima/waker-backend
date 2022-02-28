from apscheduler.schedulers.background import BackgroundScheduler

from ..settings import Settings


def create_worker(settings: Settings):
    worker = BackgroundScheduler()

    return worker
