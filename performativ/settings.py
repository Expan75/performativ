import os
from dataclasses import dataclass


@dataclass
class Settings:
    api_key: str = os.environ["PERFORMATIV_API_KEY"]
