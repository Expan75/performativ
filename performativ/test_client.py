from .client import PermformativClient


def test_httpx_client_gets_spawned(client: PermformativClient):
    assert client._client is not None
