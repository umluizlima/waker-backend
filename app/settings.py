from pydantic import BaseSettings


class Settings(BaseSettings):
    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str

    class Config:
        env_file = ".env"
        case_sensitive = True


def get_settings():
    return Settings()
