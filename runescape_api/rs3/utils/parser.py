import csv
from datetime import date, datetime, timedelta, timezone
from io import StringIO
from typing import List
from runescape_api.rs3.constants import ACTIVITIES, SKILLS
from runescape_api.rs3.models.activity_score import ActivityScore
from runescape_api.rs3.models.clan_member import ClanMember
from runescape_api.rs3.models.hiscores_lite import HiscoresLite
from runescape_api.rs3.models.skill_score import SkillScore

RUNEDATE_EPOCH = datetime(2002, 2, 27, tzinfo=timezone.utc)

def runedate_to_datetime(runedate: float) -> datetime:
    """
    Convert a RuneScape Runedate to a UTC datetime.

    Args:
        runedate (float): Number of days since 2002-02-27 00:00 UTC.

    Returns:
        datetime: Corresponding UTC datetime.
    """
    return RUNEDATE_EPOCH + timedelta(days=runedate)

def parse_rs_date(value: str) -> date:
    return datetime.strptime(value, "%d %b %Y").date()

def parse_hiscores_lite(raw: str) -> HiscoresLite:
    lines = raw.strip().splitlines()

    skills: dict[str, SkillScore] = {}
    activities: dict[str, ActivityScore] = {}

    cursor = 0

    for name in SKILLS:
        skills[name] = SkillScore.from_csv(lines[cursor])
        cursor += 1

    for name in ACTIVITIES:
        activities[name] = ActivityScore.from_csv(lines[cursor])
        cursor += 1

    return HiscoresLite(
        skills=skills,
        activities=activities,
    )

def parse_clan_member(raw: str) -> List[ClanMember]:
    reader = csv.DictReader(StringIO(raw))
    members = []
    for row in reader:
        members.append(
            ClanMember(
                player_name=row["Clanmate"].strip(),
                rank=row[" Clan Rank"].strip(),
                total_xp=int(row[" Total XP"]),
                kills=int(row[" Kills"]),
            )
        )
    return members