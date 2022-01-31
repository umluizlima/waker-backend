from sqlalchemy.orm.exc import NoResultFound

from ..errors import ResourceNotFoundError
from ..models import Call
from .base import BaseRepository


class CallRepository(BaseRepository):
    __model__ = Call

    def find_by_sid(self, sid: str) -> Call:
        try:
            return self._filter_by_sid(sid).one()
        except NoResultFound:
            raise ResourceNotFoundError

    def _filter_by_sid(self, sid: str):
        return self.db.query(self.__model__).filter(self.__model__.sid == sid)
