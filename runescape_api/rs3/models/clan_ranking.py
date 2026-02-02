from dataclasses import dataclass

@dataclass(frozen=True)
class ClanRanking:
    rank: int
    clan_name: str
    clan_mates: int
    xp_total: int

    @classmethod
    def from_response(cls, data: dict) -> "ClanRanking":
        return cls(
            rank=int(data["rank"]),
            clan_name=data["clan_name"],
            clan_mates=int(data["clan_mates"]),
            xp_total=int(data["xp_total"]),
        )