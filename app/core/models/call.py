from enum import Enum, auto

from sqlalchemy import Column, DateTime
from sqlalchemy import Enum as SqlEnum
from sqlalchemy import Text

from .base import BaseModel


class AutoName(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class CallStatus(str, AutoName):
    WAITING = auto()
    REQUESTED = auto()
    COMPLETED = auto()
    FAILED = auto()


class Call(BaseModel):
    __tablename__ = "call"

    sid = Column(Text, nullable=True)
    scheduled_to = Column(DateTime, nullable=False)
    status = Column(SqlEnum(CallStatus), default=CallStatus.WAITING, nullable=False)
