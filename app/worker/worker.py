from procrastinate import AiopgConnector, App

from app.core.tasks import blueprint
from app.settings import Settings


def create_worker(settings: Settings):
    worker = App(
        connector=AiopgConnector(dsn=settings.DATABASE_URL),
        import_paths=["app.core.tasks"],
    )
    worker.add_tasks_from(blueprint, namespace="waker-tasks")
    worker.add_tasks_from(blueprint, namespace="waker-tasks")
    worker.open()
    return worker
