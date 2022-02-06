from datetime import datetime

from pydantic import BaseModel

from app.core.models import CallStatus


class CallBase(BaseModel):
    scheduled_to: datetime


class CallCreate(CallBase):
    ...


class CallRead(CallBase):
    id: int
    created_at: datetime
    updated_at: datetime
    scheduled_to: datetime
    sid: str | None
    status: CallStatus

    class Config:
        orm_mode = True
