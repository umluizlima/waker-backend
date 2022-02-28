from fastapi import APIRouter, FastAPI

from app.settings import Settings
from app.worker import get_worker

router = APIRouter()


@router.on_event("startup")
def startup_event():
    worker = get_worker()
    worker.start()


@router.on_event("shutdown")
def shutdown_event():
    worker = get_worker()
    worker.shutdown()


def configure(app: FastAPI, settings: Settings):
    app.include_router(
        router,
        tags=["worker"],
        prefix="/api/v1",
    )
