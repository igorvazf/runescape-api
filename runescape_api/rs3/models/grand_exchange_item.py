from dataclasses import dataclass
from runescape_api.rs3.models.price_trend import PriceTrend

@dataclass(frozen=True)
class GrandExchangeItem:
    id: int
    name: str
    icon: str
    icon_large: str
    type: str
    type_icon: str
    description: str
    members: bool
    current: PriceTrend
    today: PriceTrend

    @classmethod
    def from_response(cls, data: dict) -> "GrandExchangeItem":
        return cls(
            id=int(data["id"]),
            name=data["name"],
            icon=data["icon"],
            icon_large=data["icon_large"],
            type=data["type"],
            description=data["description"],
            type_icon=data["typeIcon"],
            members=data.get("members", False),
            current=PriceTrend.from_response(data["current"]),
            today=PriceTrend.from_response(data["today"]),
        )
