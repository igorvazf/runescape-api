from dataclasses import dataclass

@dataclass(frozen=True)
class PriceTrend:
    trend: str
    price: str
    change: str

    @classmethod
    def from_response(cls, data: dict) -> "PriceTrend":
        return cls(
            trend=data["trend"],
            price=data.get("price", ""),
            change=data.get("change", ""),
        )