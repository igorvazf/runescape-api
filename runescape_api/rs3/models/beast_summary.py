from dataclasses import dataclass
from typing import Optional
import re

@dataclass
class BeastSummary:
    id: int
    label: str
    name: str
    combat_level: Optional[int] = None

    @classmethod
    def from_response(cls, data: dict) -> "BeastSummary":
        label = data.get("label", "")
        name = label
        combat_level = None

        match = re.search(r"\((\d+)\)\s*$", label)
        if match:
            combat_level = int(match.group(1))
            name = label[: match.start()].strip()

        return cls(
            id=data["value"],
            label=label,
            name=name,
            combat_level=combat_level,
        )
