from dataclasses import dataclass
from typing import List
from runescape_api.rs3.models.gim_entry import GroupIronmanEntry

@dataclass(frozen=True)
class GroupIronmanPage:
    content: List[GroupIronmanEntry]
    total_elements: int
    total_pages: int
    first: bool
    last: bool
    number_of_elements: int
    page_number: int
    size: int
    empty: bool

    @classmethod
    def from_response(cls, data: dict) -> "GroupIronmanPage":
        return cls(
            content=[GroupIronmanEntry.from_response(e) for e in data["content"]],
            total_elements=data["totalElements"],
            total_pages=data["totalPages"],
            first=data["first"],
            last=data["last"],
            number_of_elements=data["numberOfElements"],
            page_number=data["pageNumber"],
            size=data["size"],
            empty=data["empty"],
        )
