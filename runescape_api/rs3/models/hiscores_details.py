from dataclasses import dataclass
from datetime import date
from runescape_api.rs3.utils.parser import parse_rs_date

@dataclass(frozen=True)
class HiscoresDetails:
    id: int
    name: str
    title: str
    description: str
    status: str
    type: str
    days_running: int
    months_running: int
    recurrence: int
    start_date: date
    end_date: date

    @classmethod
    def from_response(cls, data: dict) -> "HiscoresDetails":
        return cls(
            id=int(data["id"]),
            name=data["name"],
            title=data["title"],
            description=data["description"],
            status=data["status"],
            type=data["type"],
            days_running=int(data["daysRunning"]),
            months_running=int(data["monthsRunning"]),
            recurrence=int(data["recurrence"]),
            start_date=parse_rs_date(data["startDate"]),
            end_date=parse_rs_date(data["endDate"]),
        )