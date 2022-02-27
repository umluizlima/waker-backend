from fastapi import APIRouter, Depends, FastAPI
from starlette.status import HTTP_201_CREATED

from app.core.repositories import CallRepository
from app.core.schemas import CallCreate, CallRead
from app.core.tasks import sum
from app.settings import Settings

from ..dependencies import call_repository

router = APIRouter()


@router.post("/calls", response_model=CallRead, status_code=HTTP_201_CREATED)
def create_call(
    call: CallCreate, call_repository: CallRepository = Depends(call_repository)
):
    sum.defer(a=1, b=5)
    return call_repository.create(call.dict())


def configure(app: FastAPI, settings: Settings):
    app.include_router(
        router,
        tags=["calls"],
        prefix="/api/v1",
    )
