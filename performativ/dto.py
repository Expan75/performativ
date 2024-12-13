from datetime import datetime
from dataclasses import dataclass
from .enums import Currency, TransactionType


@dataclass
class Window:
    start: datetime
    end: datetime


@dataclass
class Position:
    id: int
    open_date: datetime
    close_date: datetime
    open_price: float
    close_price: float
    quantity: float
    transaction_costs: float
    instrument_id: int
    instrument_currency: Currency
    open_transaction_type: TransactionType
    close_transaction_type: TransactionType


@dataclass
class FXRatesRequest:
    pairs: list[tuple[Currency, Currency]]
    window: Window


@dataclass
class FXRatesResponse:
    pass


@dataclass
class PricesRequest:
    instrument_id: str
    window: Window


@dataclass
class PricesResponse:
    pass


@dataclass
class SubmissionRequest:
    pass


@dataclass
class SubmissionResponse:
    pass
