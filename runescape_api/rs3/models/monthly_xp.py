from dataclasses import dataclass
from typing import List
from runescape_api.rs3.models.monthly_xp_entry import MonthlyXpEntry

@dataclass(frozen=True)
class MonthlyXp:
    skill_id: int
    average_xp_gain: int
    total_gain: int
    total_xp: int
    month_data: List[MonthlyXpEntry]
    logged_in: bool | None

    @classmethod
    def from_response(cls, data: dict) -> "MonthlyXp":
        monthly = data["monthlyXpGain"]

        return cls(
            skill_id=monthly["skillId"],
            average_xp_gain=monthly["averageXpGain"],
            total_gain=monthly["totalGain"],
            total_xp=monthly["totalXp"],
            month_data=[
                MonthlyXpEntry.from_response(m)
                for m in monthly.get("monthData", [])
            ],
            logged_in=(
                data["loggedIn"] == "true"
                if "loggedIn" in data
                else None
            ),
        )
