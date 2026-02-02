from typing import List
from runescape_api.rs3.constants import APPS_RS
from runescape_api.rs3.http.base_http_adapter import BaseHttpAdapter
from runescape_api.rs3.models.monthly_xp import MonthlyXp
from runescape_api.rs3.models.quest import Quest
from runescape_api.rs3.models.runemetrics_profile import RunemetricsProfile
from runescape_api.rs3.utils.validation import is_non_empty_str, is_positive_int

class Runemetrics:
    def __init__(self, http_adapter: BaseHttpAdapter):
        self.http_adapter = http_adapter

    def get_profile(self, player_name: str, activities: int) -> RunemetricsProfile:
        is_non_empty_str(player_name, "player_name")
        is_positive_int(activities, "activities")
        response = self.http_adapter.get(
            base_url=APPS_RS,
            path="/runemetrics/profile/profile",
            params={
                "user": player_name,
                "activities": activities,
            },
        )
        return RunemetricsProfile.from_response(response)
    
    def get_monthly_xp(self, player_name: str, skill_id: int) -> MonthlyXp:
        is_non_empty_str(player_name, "player_name")
        is_positive_int(skill_id, "skill_id")
        response = self.http_adapter.get(
            base_url=APPS_RS,
            path="/runemetrics/xp-monthly",
            params={
                "searchName": player_name,
                "skillid": skill_id,
            },
        )
        return MonthlyXp.from_response(response)
    
    def get_quests(self, player_name: str) -> List[Quest]:
        is_non_empty_str(player_name, "player_name")
        raw = self.http_adapter.get(
            base_url=APPS_RS,
            path="/runemetrics/quests",
            params={"user": player_name},
        )
        return [Quest.from_response(r) for r in raw]
