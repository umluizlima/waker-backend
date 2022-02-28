from fastapi import APIRouter, FastAPI

from app.settings import Settings
from app.worker.run import worker

router = APIRouter()


@router.on_event("startup")
def startup_event():
    worker.start()


@router.on_event("shutdown")
def shutdown_event():
    worker.shutdown()


def configure(app: FastAPI, settings: Settings):
    app.include_router(
        router,
        tags=["worker"],
        prefix="/api/v1",
    )
