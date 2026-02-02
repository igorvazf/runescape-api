from dataclasses import dataclass

@dataclass(frozen=True)
class GroupMember:
    id: int
    name: str

    @classmethod
    def from_response(cls, data: dict) -> "GroupMember":
        return cls(
            id=data.get("id", 0),
            name=data["name"],
        )