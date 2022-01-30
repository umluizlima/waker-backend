from fastapi import FastAPI

from app.settings import Settings

from . import call


def configure(app: FastAPI, settings: Settings):
    for router in [call]:
        router.configure(app, settings)
