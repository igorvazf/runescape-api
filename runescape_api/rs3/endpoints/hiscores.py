from typing import List
from runescape_api.rs3.constants import SECURE_RS
from runescape_api.rs3.http.base_http_adapter import BaseHttpAdapter
from runescape_api.rs3.models.clan_member import ClanMember
from runescape_api.rs3.models.clan_ranking import ClanRanking
from runescape_api.rs3.models.gim_page import GroupIronmanPage
from runescape_api.rs3.models.group_hiscores_page import GroupHiscoresPage
from runescape_api.rs3.models.hiscores_details import HiscoresDetails
from runescape_api.rs3.models.hiscores_lite import HiscoresLite
from runescape_api.rs3.models.seasonal_ranking import SeasonalRanking
from runescape_api.rs3.models.user_clan_ranking import UserClanRanking
from runescape_api.rs3.utils.parser import parse_clan_member, parse_hiscores_lite
from runescape_api.rs3.utils.validation import is_boolean, is_non_empty_str, is_positive_int

class Hiscores:
    def __init__(self, http_adapter: BaseHttpAdapter):
        self.http_adapter = http_adapter

    def get_ranking(self, table: int, category: int, size: int) -> dict:
        is_positive_int(table, "table")
        is_positive_int(category, "category")
        is_positive_int(size, "size")
        return self.http_adapter.get(
            base_url=SECURE_RS,
            path="/m=hiscore/ranking.json",
            params={
                "table": table,
                "category": category,
                "size": size,
            },
        )
    
    def get_user_ranking(self, session_id: int) -> dict:
        return self.http_adapter.get(
            base_url=SECURE_RS,
            path=f"/c={session_id}/m=hiscore/userRanking.json",
        )

    def get_hiscores_lite(self, player_name: str) -> HiscoresLite:
        is_non_empty_str(player_name, "player_name")
        raw = self.http_adapter.get(
            base_url=SECURE_RS,
            path="/m=hiscore/index_lite.ws",
            params={"player": player_name},
            raw=True,
        )
        return parse_hiscores_lite(raw)
    
    def get_ironman_lite(self, player_name: str) -> HiscoresLite:
        is_non_empty_str(player_name, "player_name")
        raw = self.http_adapter.get(
            base_url=SECURE_RS,
            path="/m=hiscore_ironman/index_lite.ws",
            params={"player": player_name},
            raw=True,
        )
        return parse_hiscores_lite(raw)
    
    def get_hardcore_ironman_lite(self, player_name: str) -> HiscoresLite:
        is_non_empty_str(player_name, "player_name")
        raw = self.http_adapter.get(
            base_url=SECURE_RS,
            path="/m=hiscore_hardcore_ironman/index_lite.ws",
            params={"player": player_name},
            raw=True,
        )
        return parse_hiscores_lite(raw)
    
    def get_leagues_lite(self, player_name: str) -> HiscoresLite:
        is_non_empty_str(player_name, "player_name")
        raw = self.http_adapter.get(
            base_url=SECURE_RS,
            path="/m=hiscore_leagues/index_lite.ws",
            params={"player": player_name},
            raw=True,
        )
        return parse_hiscores_lite(raw)
        
    def get_seasonal_ranking(self, player_name: str, archived: bool = False) -> List[SeasonalRanking]:
        is_non_empty_str(player_name, "player_name")
        params = {"player": player_name}
        if archived:
            params["status"] = "archived"
        response = self.http_adapter.get(
            base_url=SECURE_RS,
            path="/m=temp-hiscores/getRankings.json",
            params=params,
        )
        return [SeasonalRanking.from_response(r) for r in response]
    
    def get_hiscores_details(self, archived: bool = False) -> List[HiscoresDetails]:
        params = {}
        if archived:
            params["status"] = "archived"
        response = self.http_adapter.get(
            base_url=SECURE_RS,
            path="/m=temp-hiscores/getHiscoreDetails.json",
            params=params,
        )
        return [HiscoresDetails.from_response(r) for r in response]
    
    def get_clan_ranking(self) -> List[ClanRanking]:
        response = self.http_adapter.get(
            base_url=SECURE_RS,
            path="/m=clan-hiscores/clanRanking.json",
        )
        return [ClanRanking.from_response(r) for r in response]
    
    def get_user_clan_ranking(self, session_id: int) -> UserClanRanking:
        response = self.http_adapter.get(
            base_url=SECURE_RS,
            path=f"/c={session_id}/m=clan-hiscores/userClanRanking.json",
        )
        return UserClanRanking.from_response(response)
    
    def get_clan_members_lite(self, clan_name: str) -> List[ClanMember]:
        is_non_empty_str(clan_name, "clan_name")
        raw = self.http_adapter.get(
            base_url=SECURE_RS,
            path="/m=clan-hiscores/members_lite.ws",
            params={"clanName": clan_name},
            raw=True,
        )
        csv_text = raw.text
        return parse_clan_member(csv_text)
    
    def get_bosses_groups(self, group_size: int, size: int, boss_id: int, page: int) -> GroupHiscoresPage:
        is_positive_int(group_size, "group_size")
        is_positive_int(size, "size")
        is_positive_int(boss_id, "boss_id")
        is_positive_int(page, "page")
        response = self.http_adapter.get(
            base_url=SECURE_RS,
            path="/m=group_hiscores/v1//groups",
            params={
                "groupSize": group_size,
                "size": size,
                "bossId": boss_id,
                "page": page,
            },
        )
        return GroupHiscoresPage.from_response(response)
    
    def get_group_ironman(self, group_size: int, size: int, page: int, competitive: bool) -> GroupIronmanPage:
        is_positive_int(group_size, "group_size")
        is_positive_int(size, "size")
        is_positive_int(page, "page")
        is_boolean(competitive, "boss_id")
        response = self.http_adapter.get(
            base_url=SECURE_RS,
            path="/m=runescape_gim_hiscores//v1/groupScores",
            params={
                "groupSize": group_size,
                "size": size,
                "page": page,
                "isCompetitive": competitive, # str(competitive).lower(),
            },
        )
        return GroupIronmanPage.from_response(response)