from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class Beast:
    id: int
    name: str
    members: bool
    weakness: str
    combat_level: int
    life_points: int
    defence_level: int
    attack_level: int
    magic_level: int
    ranged_level: int
    experience: str
    slayer_level: Optional[int]
    slayer_category: Optional[str]
    size: int
    attackable: bool
    aggressive: bool
    poisonous: bool
    description: str
    areas: List[str]
    animations: Dict[str, int]

    @classmethod
    def from_response(cls, data: dict) -> "Beast":
        return cls(
            id=data["id"],
            name=data["name"],
            members=data.get("members", False),
            weakness=data.get("weakness", ""),
            combat_level=data.get("level", 0),
            life_points=data.get("lifePoints", 0),
            defence_level=data.get("defence", 0),
            attack_level=data.get("attack", 0),
            magic_level=data.get("magic", 0),
            ranged_level=data.get("ranged", 0),
            experience=data.get("xp", ""),
            slayer_level=data.get("slayerlevel"),
            slayer_category=data.get("slayerCategory"),
            size=data.get("size", 0),
            attackable=data.get("attackable", False),
            aggressive=data.get("aggressive", False),
            poisonous=data.get("poisonous", False),
            description=data.get("description", ""),
            areas=data.get("areas", []),
            animations=data.get("animations", {}),
        )
