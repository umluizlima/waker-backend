from pydantic import BaseSettings


class Settings(BaseSettings):
    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_FROM_NUMBER: str
    TWILIO_TO_NUMBER: str
    DEFAULT_MESSAGE: str = (
        "Hello! You asked to be awake at this time. Have a great day!"
    )

    class Config:
        env_file = ".env"
        case_sensitive = True


def get_settings():
    return Settings()
