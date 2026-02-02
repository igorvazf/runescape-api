from dataclasses import dataclass

@dataclass(frozen=True)
class MonthlyXpEntry:
    month: str
    xp: int

    @classmethod
    def from_response(cls, data: dict) -> "MonthlyXpEntry":
        return cls(
            month=data["month"],
            xp=data["xp"],
        )
