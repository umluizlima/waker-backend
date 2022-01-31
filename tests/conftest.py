from pytest import fixture

from app.settings import Settings


@fixture
def settings():
    return get_test_settings()


def get_test_settings():
    return Settings(
        _env_file=None,
        TWILIO_ACCOUNT_SID="abcdef",
        TWILIO_AUTH_TOKEN="abcdef",
        TWILIO_FROM_NUMBER="+1222333444",
        TWILIO_TO_NUMBER="+2333444555",
    )
