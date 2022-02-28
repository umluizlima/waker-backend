from fastapi import APIRouter, Depends, FastAPI
from starlette.status import HTTP_201_CREATED

from app.core.schemas import CallCreate, CallRead
from app.core.services import CallService
from app.settings import Settings

from ..dependencies import call_service

router = APIRouter()


@router.post("/calls", response_model=CallRead, status_code=HTTP_201_CREATED)
def create_call(call: CallCreate, call_service: CallService = Depends(call_service)):
    return call_service.create_call(call)


def configure(app: FastAPI, settings: Settings):
    app.include_router(
        router,
        tags=["calls"],
        prefix="/api/v1",
    )
