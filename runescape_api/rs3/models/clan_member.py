from dataclasses import dataclass

@dataclass(frozen=True)
class ClanMember:
    player_name: str
    rank: str
    total_xp: int
    kills: int