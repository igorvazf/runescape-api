from dataclasses import dataclass

@dataclass(frozen=True)
class UserClanRanking:
    display_name: str
    clan_name: str
    clan_rank: int

    @classmethod
    def from_response(cls, data: dict) -> "UserClanRanking":
        return cls(
            display_name=data["displayName"],
            clan_name=data["clanName"],
            clan_rank=int(data["clanRank"]),
        )