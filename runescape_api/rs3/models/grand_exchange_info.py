from dataclasses import dataclass
from datetime import datetime
from runescape_api.rs3.utils.parser import runedate_to_datetime

@dataclass(frozen=True)
class GrandExchangeInfo:
    runedate: float
    last_update: datetime

    @classmethod
    def from_response(cls, data: dict) -> "GrandExchangeInfo":
        runedate = float(data["lastConfigUpdateRuneday"])
        return cls(
            runedate=runedate,
            last_update=runedate_to_datetime(runedate),
        )
