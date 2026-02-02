from dataclasses import dataclass
from datetime import date
from runescape_api.rs3.utils.parser import parse_rs_date

@dataclass(frozen=True)
class SeasonalRanking:
    hiscore_id: int
    title: str
    rank: int
    score_formatted: str
    score_raw: int
    start_date: date
    end_date: date

    @classmethod
    def from_response(cls, data: dict) -> "SeasonalRanking":
        return cls(
            hiscore_id=int(data["hiscoreId"]),
            title=data["title"],
            rank=int(data["rank"]),
            score_formatted=data["score_formatted"],
            score_raw=int(data["score_raw"]),
            start_date=parse_rs_date(data["startDate"]),
            end_date=parse_rs_date(data["endDate"]),
        )