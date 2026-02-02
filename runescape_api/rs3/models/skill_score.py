from dataclasses import dataclass

@dataclass(frozen=True)
class SkillScore:
    rank: int
    level: int
    experience: int

    @classmethod
    def from_csv(cls, line: str) -> "SkillScore":
        rank, level, xp = map(int, line.split(","))
        return cls(rank=rank, level=level, experience=xp)