from dataclasses import dataclass
from typing import List
from runescape_api.rs3.models.group_kill_entry import GroupKillEntry

@dataclass(frozen=True)
class GroupHiscoresPage:
    content: List[GroupKillEntry]
    total_elements: int
    total_pages: int
    first: bool
    last: bool
    number_of_elements: int
    number: int
    size: int
    empty: bool

    @classmethod
    def from_response(cls, data: dict) -> "GroupHiscoresPage":
        return cls(
            content=[GroupKillEntry.from_response(e) for e in data["content"]],
            total_elements=data["totalElements"],
            total_pages=data["totalPages"],
            first=data["first"],
            last=data["last"],
            number_of_elements=data["numberOfElements"],
            number=data["number"],
            size=data["size"],
            empty=data["empty"],
        )
