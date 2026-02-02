from typing import Dict, List
from runescape_api.rs3.constants import SERVICES_RS
from runescape_api.rs3.http.base_http_adapter import BaseHttpAdapter
from runescape_api.rs3.models.beast import Beast
from runescape_api.rs3.models.beast_summary import BeastSummary
from runescape_api.rs3.utils.validation import is_non_empty_str, is_positive_int

class Bestiary:
    def __init__(self, http_adapter: BaseHttpAdapter):
        self.http_adapter = http_adapter

    def get_beast_by_id(self, beast_id: int) -> Beast:
        """
        Get specific statistics and information on a specific monster.

        Args:
            beast_id (int): Unique identifier of the beast. Must be a positive integer.

        Returns:
            Beast: A Beast model populated with the API response data.

        Raises:
            TypeError: If beast_id is not an integer.
            ValueError: If beast_id is not a positive integer.
            RuneScapeApiException: If the RuneScape API returns an error response.
            TimeoutError: If the request times out.
        """
        is_positive_int(beast_id, "beast_id")
        response = self.http_adapter.get(
            base_url=SERVICES_RS,
            path="/m=itemdb_rs/bestiary/beastData.json",
            params={"beastid": beast_id}
        )
        return Beast.from_response(response)
    
    def get_beasts_by_term(self, term: str) -> List[BeastSummary]:
        is_non_empty_str(term, "term")
        response = self.http_adapter.get(
            base_url=SERVICES_RS,
            path="/m=itemdb_rs/bestiary/beastSearch.json",
            params={"term": term},
        )
        return [BeastSummary.from_response(r) for r in response]
    
    def get_beasts_by_letter(self, letter: str) -> List[BeastSummary]:
        is_non_empty_str(letter, "letter")
        response = self.http_adapter.get(
            base_url=SERVICES_RS,
            path="/m=itemdb_rs/bestiary/bestiaryNames.json",
            params={"letter": letter},
        )
        return [BeastSummary.from_response(r) for r in response]
    
    def get_area_names(self) -> List[str]:
        return self.http_adapter.get(
            base_url=SERVICES_RS,
            path="/m=itemdb_rs/bestiary/areaNames.json",
        )
    
    def get_beasts_by_area(self, area_name: str) -> List[BeastSummary]:
        is_non_empty_str(area_name, "area_name")
        response = self.http_adapter.get(
            base_url=SERVICES_RS,
            path="/m=itemdb_rs/bestiary/areaBeasts.json",
            params={"identifier": area_name},
        )
        return [BeastSummary.from_response(r) for r in response]

    def get_slayer_categories(self) -> Dict[int, str]:
        return self.http_adapter.get(
            base_url=SERVICES_RS,
            path="/m=itemdb_rs/bestiary/slayerCatNames.json",
        )
    
    def get_beasts_by_slayer_category(self, category: int) -> List[BeastSummary]:
        is_positive_int(category, "category")
        response = self.http_adapter.get(
            base_url=SERVICES_RS,
            path="/m=itemdb_rs/bestiary/slayerBeasts.json",
            params={"identifier": category},
        )
        return [BeastSummary.from_response(r) for r in response]
    
    def get_weakness(self) -> Dict[int, str]:
        return self.http_adapter.get(
            base_url=SERVICES_RS,
            path="/m=itemdb_rs/bestiary/weaknessNames.json",
        )

    def get_beasts_by_weakness(self, weakness: int) -> List[BeastSummary]:
        is_positive_int(weakness, "weakness")
        response = self.http_adapter.get(
            base_url=SERVICES_RS,
            path="/m=itemdb_rs/bestiary/weaknessBeasts.json",
            params={"identifier": weakness},
        )
        return [BeastSummary.from_response(r) for r in response]
    
    def get_beasts_by_level_range(self, lower_threshold: int, upper_threshold: int) -> List[BeastSummary]:
        response = self.http_adapter.get(
            base_url=SERVICES_RS,
            path="/m=itemdb_rs/bestiary/levelGroup.json",
            params={"identifier": f"{lower_threshold}-{upper_threshold}"},
        )
        return [BeastSummary.from_response(r) for r in response]
