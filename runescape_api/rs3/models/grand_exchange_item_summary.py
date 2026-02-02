from dataclasses import dataclass
from typing import List
from runescape_api.rs3.models.grand_exchange_item import GrandExchangeItem

@dataclass(frozen=True)
class GrandExchangeItemSummary:
    total: int
    items: List[GrandExchangeItem]

    @classmethod
    def from_response(cls, data: dict) -> "GrandExchangeItemSummary":
        return cls(
            total=int(data["total"]),
            items=[
                GrandExchangeItem.from_response(item)
                for item in data["items"]
            ],
        )