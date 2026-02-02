from dataclasses import dataclass
from datetime import datetime
from typing import List
from runescape_api.rs3.models.group_member import GroupMember

@dataclass(frozen=True)
class GroupKillEntry:
    id: int
    boss_id: int
    group_size: int
    rank: int
    enrage: int
    kill_time_seconds: float
    time_of_kill: datetime
    members: List[GroupMember]

    @classmethod
    def from_response(cls, data: dict) -> "GroupKillEntry":
        return cls(
            id=data["id"],
            boss_id=data["bossId"],
            group_size=data["size"],
            rank=data["rank"],
            enrage=data["enrage"],
            kill_time_seconds=float(data["killTimeSeconds"]),
            time_of_kill=datetime.utcfromtimestamp(data["timeOfKill"]),
            members=[GroupMember.from_response(m) for m in data["members"]],
        )