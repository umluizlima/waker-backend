from fastapi import FastAPI

from app.settings import Settings

from . import call, worker


def configure(app: FastAPI, settings: Settings):
    for router in [call, worker]:
        router.configure(app, settings)
