from dataclasses import dataclass

@dataclass(frozen=True)
class GroupIronmanEntry:
    id: int
    name: str
    group_total_xp: int
    group_total_level: int
    size: int
    to_highlight: bool
    is_competitive: bool
    founder: bool

    @classmethod
    def from_response(cls, data: dict) -> "GroupIronmanEntry":
        return cls(
            id=data["id"],
            name=data["name"],
            group_total_xp=data["groupTotalXp"],
            group_total_level=data["groupTotalLevel"],
            size=data["size"],
            to_highlight=data["toHighlight"],
            is_competitive=data["isCompetitive"],
            founder=data["founder"],
        )
