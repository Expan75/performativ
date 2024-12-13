import pytest
from performativ.client import PermformativClient


@pytest.fixture
def client():
    return PermformativClient(api_key="notvalid")
