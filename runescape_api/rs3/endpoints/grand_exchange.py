import json
from runescape_api.rs3.constants import ITEM_CATEGORIES, SECURE_RS, SERVICES_RS
from runescape_api.rs3.http.base_http_adapter import BaseHttpAdapter
from runescape_api.rs3.models.grand_exchange_info import GrandExchangeInfo
from runescape_api.rs3.models.grand_exchange_item_detail import GrandExchangeItemDetail
from runescape_api.rs3.models.grand_exchange_item_summary import GrandExchangeItemSummary
from runescape_api.rs3.utils.validation import is_non_empty_str, is_positive_int

class GrandExchange:
    def __init__(self, http_adapter: BaseHttpAdapter):
        self.http_adapter = http_adapter

    def get_last_update(self) -> GrandExchangeInfo:
        response = self.http_adapter.get(
            base_url=SECURE_RS,
            path="/m=itemdb_rs/api/info.json",
        )
        return GrandExchangeInfo.from_response(response)
    
    def get_categories(self) -> list:
        data = [{"id": key,"name": value} for key, value in ITEM_CATEGORIES.items()]
        return json.dumps(data)
    
    def get_number_of_items_by_category(self, category_id: int) -> dict:
        is_positive_int(category_id, "category_id")
        return self.http_adapter.get(
            base_url=SECURE_RS,
            path="/m=itemdb_rs/api/catalogue/category.json",
            params={"category": category_id},
        )
    
    def get_items(self, category_id: int, starting_letter: str, page_number: int) -> GrandExchangeItemSummary:
        is_positive_int(category_id, "category_id")
        is_non_empty_str(starting_letter, "starting_letter")
        is_positive_int(page_number, "page_number")
        response = self.http_adapter.get(
            base_url=SECURE_RS,
            path="/m=itemdb_rs/api/catalogue/items.json",
            params={
                "category": category_id,
                "alpha": starting_letter,
                "page": page_number,
            },
        )
        return GrandExchangeItemSummary.from_response(response)

    def get_item_detail(self, item_id: int) -> GrandExchangeItemDetail:
        is_positive_int(item_id, "item_id")
        response = self.http_adapter.get(
            base_url=SECURE_RS,
            path="/m=itemdb_rs/api/catalogue/detail.json",
            params={"item": item_id},
        )
        return GrandExchangeItemDetail.from_response(response["item"])
    
    def get_item_graph(self, item_id: int) -> dict:
        is_positive_int(item_id, "item_id")
        return self.adapter.get(
            base_url=SECURE_RS,
            path=f"/m=itemdb_rs/api/graph/{item_id}.json",
        )
