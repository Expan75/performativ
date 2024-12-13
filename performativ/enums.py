from enum import StrEnum


class Currency(StrEnum):
    USD = "USD"
    GBP = "GBP"
    DKK = "DKK"


class TransactionType(StrEnum):
    BUY = "BUY"
    SELL = "SELL"
