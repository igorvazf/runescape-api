from dataclasses import dataclass

@dataclass(frozen=True)
class ActivityScore:
    rank: int
    score: int

    @classmethod
    def from_csv(cls, line: str) -> "ActivityScore":
        rank, score = map(int, line.split(","))
        return cls(rank=rank, score=score)