import json
import pytest
from unittest.mock import Mock
from runescape_api.rs3.constants import ITEM_CATEGORIES, SECURE_RS
from runescape_api.rs3.endpoints.grand_exchange import GrandExchange
from runescape_api.rs3.http.base_http_adapter import BaseHttpAdapter
from runescape_api.rs3.models.grand_exchange_info import GrandExchangeInfo
from runescape_api.rs3.models.grand_exchange_item_detail import GrandExchangeItemDetail
from runescape_api.rs3.models.grand_exchange_item_summary import GrandExchangeItemSummary

class TestGrandExchange:

    @pytest.fixture
    def mock_http_adapter(self):
        adapter = Mock(spec=BaseHttpAdapter)
        return adapter
    
    @pytest.fixture
    def grand_exchange(self, mock_http_adapter):
        grand_exchange = GrandExchange(mock_http_adapter)
        return grand_exchange
    
    def test_get_last_update_success(self, grand_exchange, mock_http_adapter):
        mock_http_adapter.get.return_value = {"lastConfigUpdateRuneday":8793}

        result = grand_exchange.get_last_update()

        mock_http_adapter.get.assert_called_once()
        assert isinstance(result, GrandExchangeInfo)
    
    def test_get_categories_content(self, grand_exchange):
        result = grand_exchange.get_categories()
        data = json.loads(result)

        expected = [
            {"id": key, "name": value}
            for key, value in ITEM_CATEGORIES.items()
        ]

        assert data == expected
    
    def test_get_number_of_items_by_category_success(self, grand_exchange, mock_http_adapter):
        expected_response = {
            "types": [],
            "alpha": [
                {"letter":"#","items":0},
                {"letter":"a","items":6},
                {"letter":"b","items":8},
                {"letter":"c","items":1},
                {"letter":"d","items":3},
                {"letter":"e","items":2},
                {"letter":"f","items":3},
                {"letter":"g","items":5},
                {"letter":"h","items":2},
                {"letter":"i","items":5},
                {"letter":"j","items":0},
                {"letter":"k","items":1},
                {"letter":"l","items":2},
                {"letter":"m","items":5},
                {"letter":"n","items":1},
                {"letter":"o","items":1},
                {"letter":"p","items":4},
                {"letter":"q","items":0},
                {"letter":"r","items":3},
                {"letter":"s","items":27},
                {"letter":"t","items":2},
                {"letter":"u","items":1},
                {"letter":"v","items":5},
                {"letter":"w","items":2},
                {"letter":"x","items":0},
                {"letter":"y","items":0},
                {"letter":"z","items":0}
            ]
        }

        mock_http_adapter.get.return_value = expected_response

        result = grand_exchange.get_number_of_items_by_category(9)

        mock_http_adapter.get.assert_called_once_with(
            base_url=SECURE_RS,
            path="/m=itemdb_rs/api/catalogue/category.json",
            params={"category": 9},
        )

        assert isinstance(result, dict)
    
    def test_get_items_success(self, grand_exchange, mock_http_adapter):
        expected_response = {
            "total": 98,
            "items": [
                {
                    "icon": "https://secure.runescape.com/m=itemdb_rs/1760350970334_obj_sprite.gif?id=12091",
                    "icon_large": "https://secure.runescape.com/m=itemdb_rs/1760350970334_obj_big.gif?id=12091",
                    "id": 12091,
                    "type": "Familiars",
                    "typeIcon": "https://www.runescape.com/img/categories/Familiars",
                    "name": "Compost mound pouch",
                    "description": "I can summon a compost mound familiar with this.",
                    "current": {"trend":"neutral","price":888},
                    "today": {"trend":"neutral","price":0},
                    "members": "true"
                }
            ]
        }

        mock_http_adapter.get.return_value = expected_response

        result = grand_exchange.get_items(9,"c",1)

        mock_http_adapter.get.assert_called_once_with(
            base_url=SECURE_RS,
            path="/m=itemdb_rs/api/catalogue/items.json",
            params={"category": 9, "alpha": "c", "page": 1},
        )

        assert isinstance(result, GrandExchangeItemSummary)
    
    def test_get_item_detail_success(self, grand_exchange, mock_http_adapter):
        expected_response = {
            "item": {
                "icon": "https://secure.runescape.com/m=itemdb_rs/1760350970334_obj_sprite.gif?id=21787",
                "icon_large": "https://secure.runescape.com/m=itemdb_rs/1760350970334_obj_big.gif?id=21787",
                "id": 21787,
                "type": "Miscellaneous",
                "typeIcon": "https://www.runescape.com/img/categories/Miscellaneous",
                "name": "Steadfast boots",
                "description": "A pair of powerful-looking boots.",
                "current": {"trend":"neutral","price":"5.2m"},
                "today": {"trend":"neutral","price":0},
                "members": "true",
                "day30": {"trend":"negative","change":"-2.0%"},
                "day90": {"trend":"negative","change":"-6.0%"},
                "day180": {"trend":"positive","change":"+2.0%"}
            }
        }

        mock_http_adapter.get.return_value = expected_response

        result = grand_exchange.get_item_detail(21787)

        mock_http_adapter.get.assert_called_once_with(
            base_url=SECURE_RS,
            path="/m=itemdb_rs/api/catalogue/detail.json",
            params={"item": 21787},
        )

        assert isinstance(result, GrandExchangeItemDetail)

    def test_get_item_graph_success(self, grand_exchange, mock_http_adapter):
        expected_response = {
            "daily": {"1419897600000": 15633853, "1419984000000": 15475988, "1420070400000": 15379017},
            "average": {"1419897600000": 14708793, "1419984000000": 14764787, "1420070400000": 148288055}
        }

        mock_http_adapter.get.return_value = expected_response

        result = grand_exchange.get_item_graph(21787)

        mock_http_adapter.get.assert_called_once_with(
            base_url=SECURE_RS,
            path="/m=itemdb_rs/api/graph/21787.json",
        )

        assert isinstance(result, dict)