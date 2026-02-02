from dataclasses import dataclass
from runescape_api.rs3.models.activity_score import ActivityScore
from runescape_api.rs3.models.skill_score import SkillScore

@dataclass(frozen=True)
class HiscoresLite:
    skills: dict[str, SkillScore]
    activities: dict[str, ActivityScore]