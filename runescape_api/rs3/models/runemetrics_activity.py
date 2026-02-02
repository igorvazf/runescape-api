from dataclasses import dataclass

@dataclass(frozen=True)
class RunemetricsActivity:
    date: str
    details: str
    text: str

    @classmethod
    def from_response(cls, data: dict) -> "RunemetricsActivity":
        return cls(
            date=data["date"],
            details=data["details"],
            text=data["text"],
        )
