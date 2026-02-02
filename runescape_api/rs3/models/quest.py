from dataclasses import dataclass

@dataclass(frozen=True)
class Quest:
    title: str
    status: str
    difficulty: int
    members: bool
    quest_points: int
    user_eligible: bool

    @classmethod
    def from_response(cls, data: dict) -> "Quest":
        return cls(
            title=data["title"],
            status=data["status"],
            difficulty=data["difficulty"],
            members=data["members"],
            quest_points=data["questPoints"],
            user_eligible=data["userEligible"],
        )
