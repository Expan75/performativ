from httpx import Client
from .dto import (
    FXRatesRequest,
    FXRatesResponse,
    PricesRequest,
    PricesResponse,
    SubmissionRequest,
    SubmissionResponse,
)


class PermformativClient:

    @property
    def _headers(self) -> dict:
        return {
            "Content-type": "application/json",
            "Accept": "application/json",
            "x-api-key": self._api_key,
        }

    def __init__(
        self, api_key: str, endpoint: str = "https://api.challenges.performativ.com/"
    ):
        self._api_key = api_key
        self._endpoint = endpoint
        self._client = Client(headers=self._headers)

    def get_fx_rates(self, request: FXRatesRequest) -> FXRatesResponse:
        return FXRatesResponse()

    def get_prices(self, request: PricesRequest) -> PricesResponse:
        return PricesResponse()

    def submit(self, request: SubmissionRequest) -> SubmissionResponse:
        return SubmissionResponse()
