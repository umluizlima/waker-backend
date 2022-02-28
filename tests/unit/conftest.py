from unittest.mock import Mock

from pytest import fixture


@fixture
def call_repository():
    return Mock()


@fixture
def twilio_adapter():
    return Mock()


@fixture
def worker():
    return Mock()
