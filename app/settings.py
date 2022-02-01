from enum import Enum

from pydantic import BaseSettings


class Environment(str, Enum):
    DEVELOPMENT = "dev"
    PRODUCTION = "prod"
    TEST = "test"


class EnvironmentSettings(BaseSettings):
    ENV: Environment = Environment.DEVELOPMENT


class Settings(EnvironmentSettings):
    TWILIO_ACCOUNT_SID: str
    TWILIO_AUTH_TOKEN: str
    TWILIO_FROM_NUMBER: str
    TWILIO_TO_NUMBER: str
    DEFAULT_MESSAGE: str = (
        "Hello! You asked to be awake at this time. Have a great day!"
    )
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost/waker"

    class Config:
        env_file = ".env"
        case_sensitive = True


def get_settings():
    return (
        Settings(_env_file="test.env")
        if EnvironmentSettings().ENV == Environment.TEST
        else Settings()
    )
