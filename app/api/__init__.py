from fastapi import FastAPI

from ..settings import Settings
from . import routers


def create_api(settings: Settings):
    api = FastAPI(title="waker")

    for resource in [routers]:
        resource.configure(api, settings)

    return api
