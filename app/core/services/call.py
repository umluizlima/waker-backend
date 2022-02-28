from app.core.adapters import TwilioAdapter
from app.core.models import Call, CallStatus
from app.core.repositories import CallRepository
from app.core.schemas import CallCreate
from app.settings import Settings
from app.worker import Worker


class CallService:
    def __init__(
        self,
        settings: Settings,
        adapter: TwilioAdapter,
        repository: CallRepository,
        worker: Worker,
    ) -> None:
        self._settings = settings
        self._adapter = adapter
        self._repository = repository
        self._worker = worker

    def make_call(self, call_id: int) -> None:
        call = self._repository.find_by_id(call_id)
        response = self._adapter.create_call(
            self._settings.TWILIO_FROM_NUMBER,
            self._settings.TWILIO_TO_NUMBER,
            self._adapter.build_voice_response(self._settings.DEFAULT_MESSAGE),
        )
        call.sid = response.sid
        call.status = CallStatus.REQUESTED
        self._repository.save(call, commit=True)

    def create_call(self, call: CallCreate) -> Call:
        new_call = self._repository.create(call.dict())
        self._worker.add_job(
            func=self.make_call,
            args=[new_call.id],
            trigger="date",
            run_date=new_call.scheduled_to,
            id=f"call_{new_call.id}",
        )
        return new_call
