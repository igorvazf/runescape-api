from dataclasses import dataclass

@dataclass(frozen=True)
class RunemetricsSkillValue:
    id: int
    level: int
    xp: int
    rank: int

    @classmethod
    def from_response(cls, data: dict) -> "RunemetricsSkillValue":
        return cls(
            id=data["id"],
            level=data["level"],
            xp=data["xp"],
            rank=data["rank"],
        )
