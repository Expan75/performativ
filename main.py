from performativ.client import PermformativClient
from performativ.settings import Settings


def main() -> str:
    settings = Settings()
    client = PermformativClient(api_key=settings.api_key)

    return "Hello from performativ!"
