from dataclasses import dataclass

@dataclass(frozen=True)
class PriceTrend:
    trend: str
    price: int

    @classmethod
    def from_response(cls, data: dict) -> "PriceTrend":
        return cls(
            trend=data["trend"],
            price=int(data["price"]),
        )