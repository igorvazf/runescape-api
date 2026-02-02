from dataclasses import dataclass
from typing import List
from runescape_api.rs3.models.runemetrics_activity import RunemetricsActivity
from runescape_api.rs3.models.runemetrics_skill_value import RunemetricsSkillValue

@dataclass(frozen=True)
class RunemetricsProfile:
    name: str
    rank: str
    total_skill: int
    total_xp: int
    combat_level: int

    magic_xp: int
    melee_xp: int
    ranged_xp: int

    quests_started: int
    quests_complete: int
    quests_not_started: int

    logged_in: bool

    activities: List[RunemetricsActivity]
    skill_values: List[RunemetricsSkillValue]

    @classmethod
    def from_response(cls, data: dict) -> "RunemetricsProfile":
        return cls(
            name=data["name"],
            rank=data["rank"],
            total_skill=data["totalskill"],
            total_xp=data["totalxp"],
            combat_level=data["combatlevel"],
            magic_xp=data["magic"],
            melee_xp=data["melee"],
            ranged_xp=data["ranged"],
            quests_started=data["questsstarted"],
            quests_complete=data["questscomplete"],
            quests_not_started=data["questsnotstarted"],
            logged_in=data["loggedIn"] == "true",
            activities=[RunemetricsActivity.from_response(a) for a in data.get("activities", [])],
            skill_values=[RunemetricsSkillValue.from_response(s) for s in data.get("skillvalues", [])],
        )
