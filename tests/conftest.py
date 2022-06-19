import pytest

from ..sources.main import application


@pytest.fixture
def client():
    yield application.test_client()
