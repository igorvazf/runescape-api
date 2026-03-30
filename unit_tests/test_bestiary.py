import pytest
from unittest.mock import Mock
from runescape_api.rs3.constants import SERVICES_RS
from runescape_api.rs3.endpoints.bestiary import Bestiary
from runescape_api.rs3.http.base_http_adapter import BaseHttpAdapter
from runescape_api.rs3.models.beast import Beast
from runescape_api.rs3.models.beast_summary import BeastSummary
from runescape_api.rs3.exceptions import RuneScapeApiException

class TestBestiary:
    
    @pytest.fixture
    def mock_http_adapter(self):
        adapter = Mock(spec=BaseHttpAdapter)
        return adapter
    
    @pytest.fixture
    def bestiary(self, mock_http_adapter):
        bestiary = Bestiary(mock_http_adapter)
        return bestiary
    
    def test_get_beast_by_id_success(self, bestiary, mock_http_adapter):
        expected_response = {
            "magic": 1,
            "defence": 24,
            "level": 33,
            "description": "A unicorn with a blackened heart.",
            "areas": ["RuneScape Surface"],
            "poisonous": False,
            "weakness": "Arrow",
            "size": 2,
            "ranged": 1,
            "attack": 24,
            "members": True,
            "animations": { "death": 33043, "attack": 33044 },
            "name": "Black unicorn",
            "xp": "100.8",
            "lifepoints": 3900,
            "id": 133,
            "aggressive": False,
            "attackable": True
        }
        mock_http_adapter.get.return_value = expected_response
        
        # Act
        result = bestiary.get_beast_by_id(133)
        
        # Assert
        mock_http_adapter.get.assert_called_once_with(
            base_url=SERVICES_RS,
            path="/m=itemdb_rs/bestiary/beastData.json",
            params={"beastid": 133}
        )
        assert isinstance(result, Beast)
    
    def test_get_beast_by_id_invalid_type(self, bestiary):
        with pytest.raises(TypeError):
            bestiary.get_beast_by_id("not_an_int")
    
    def test_get_beast_by_id_non_positive(self, bestiary):
        with pytest.raises(ValueError):
            bestiary.get_beast_by_id(-2)
    
    def test_get_beast_by_id_api_error(self, bestiary, mock_http_adapter):
        mock_http_adapter.get.side_effect = RuneScapeApiException()
        
        with pytest.raises(RuneScapeApiException):
            bestiary.get_beast_by_id(123)
    
    def test_get_beasts_by_term_success(self, bestiary, mock_http_adapter):
        expected_response = [
            {"label": "Unicorn (15)", "value": 89},
            {"label": "Black unicorn (33)", "value": 133},
            {"label": "Angry unicorn (45)", "value": 3646},
            {"label": "Unicorn stallion (105)", "value": 6823}
        ]

        mock_http_adapter.get.return_value = expected_response

        result = bestiary.get_beasts_by_term("Unicorn")

        mock_http_adapter.get.assert_called_once_with(
            base_url=SERVICES_RS,
            path="/m=itemdb_rs/bestiary/beastSearch.json",
            params={"term": "Unicorn"},
        )

        assert isinstance(result, list)
        assert all(isinstance(x, BeastSummary) for x in result)
        assert len(result) == 4
    
    def test_get_beasts_by_term_empty_string(self, bestiary):
        with pytest.raises(ValueError):
            bestiary.get_beasts_by_term("")
    
    def test_get_beasts_by_letter_success(self, bestiary, mock_http_adapter):
        expected_response = [
            {"label": "Qaseem", "value": 24764},
            {"label": "Qat", "value": 24422},
            {"label": "Quarry overseer", "value": 18604},
            {
                "npcs": [
                    {"label": "Quartermaster", "value": 1208},
                    {"label": "Quartermaster", "value": 19284}
                ],
                "dupe": "Quartermaster"
            },
            {
                "npcs": [
                    {"label": "Queen Black Dragon (900)", "value": 15454},
                    {"label": "Queen Black Dragon (900)", "value": 15506},
                    {"label": "Queen Black Dragon (900)", "value": 15507}
                ],
                "dupe": "Queen Black Dragon"
            },
            {
                "npcs": [
                    {"label": "Queen of Snow", "value": 6731},
                    {"label": "Queen of Snow", "value": 13642},
                    {"label": "Queen of Snow", "value": 13645}
                ],
                "dupe": "Queen of Snow"
            },
            {"label": "Queen of Sunrise", "value": 13643},
            {"label": "Queen spawn (69)", "value": 5248},
            {"label": "Querci", "value": 21408},
            {"label": "Quercus", "value": 17065},
            {"label": "Quercy", "value": 21407},
            {"label": "Quest guide", "value": 25276},
            {"label": "Quetzathog (133)", "value": 26210},
            {"label": "Quiz Master", "value": 2477}
        ]

        mock_http_adapter.get.return_value = expected_response

        result = bestiary.get_beasts_by_letter("Q")

        mock_http_adapter.get.assert_called_once_with(
            base_url=SERVICES_RS,
            path="/m=itemdb_rs/bestiary/bestiaryNames.json",
            params={"letter": "Q"},
        )

        assert isinstance(result, list)
        assert all(isinstance(x, BeastSummary) for x in result)
        assert len(result) == 19
    
    def test_get_area_names_success(self, bestiary, mock_http_adapter):
        mock_http_adapter.get.return_value = ["Agility Pyramid", "Barbarian Assault", "Dragonkin Castle"]

        result = bestiary.get_area_names()

        mock_http_adapter.get.assert_called_once()
        assert result == ["Agility Pyramid", "Barbarian Assault", "Dragonkin Castle"]
    
    def test_get_beasts_by_area_success(self, bestiary, mock_http_adapter):
        expected_response = [
            {"label": "Abyssal demon (98)", "value": 1615},
            {"label": "Abyssal guardian (79)", "value": 2264},
            {"label": "Abyssal leech (72)", "value": 2263},
            {"label": "Abyssal walker (77)", "value": 2265},
            {"label": "Dark mage", "value": 2262}
        ]

        mock_http_adapter.get.return_value = expected_response

        result = bestiary.get_beasts_by_area("The Abyss")

        mock_http_adapter.get.assert_called_once_with(
            base_url=SERVICES_RS,
            path="/m=itemdb_rs/bestiary/areaBeasts.json",
            params={"identifier": "The Abyss"},
        )

        assert isinstance(result, list)
        assert all(isinstance(x, BeastSummary) for x in result)
        assert len(result) == 5
    
    def test_get_beasts_by_area_invalid_type(self, bestiary):
        with pytest.raises(TypeError):
            bestiary.get_beasts_by_area(1)
    
    def test_get_slayer_categories_success(self, bestiary, mock_http_adapter):
        mock_http_adapter.get.return_value = {"Aberrant spectres": 41, "Dinosaurs": 171, "Onyx dragons": 137, "Rats": 3}

        result = bestiary.get_slayer_categories()

        mock_http_adapter.get.assert_called_once()
        assert result == {"Aberrant spectres": 41, "Dinosaurs": 171, "Onyx dragons": 137, "Rats": 3}
    
    def test_get_beast_by_slayer_category_success(self, bestiary, mock_http_adapter):
        expected_response = [
            {"label": "Giant worm (72)", "value": 15464},
            {"label": "Grotworm (63)", "value": 15462},
            {"label": "Mature grotworm (98)", "value": 15463},
            {"label": "Young grotworm (28)", "value": 15461}
        ]
        mock_http_adapter.get.return_value = expected_response
        
        result = bestiary.get_beasts_by_slayer_category(112)
        
        mock_http_adapter.get.assert_called_once_with(
            base_url=SERVICES_RS,
            path="/m=itemdb_rs/bestiary/slayerBeasts.json",
            params={"identifier": 112}
        )
        assert isinstance(result, list)
        assert all(isinstance(x, BeastSummary) for x in result)
        assert len(result) == 4
    
    def test_get_weakness_success(self, bestiary, mock_http_adapter):
        mock_http_adapter.get.return_value = {"Air":1,"Arrow":9,"Bolt":10,"Crushing":8,"Earth":3,"Fire":4,"Necromancy":6,"None":0,"Slashing":7,"Stabbing":5,"Thrown":11,"Water":2}

        result = bestiary.get_weakness()

        mock_http_adapter.get.assert_called_once()
        assert result == {"Air":1,"Arrow":9,"Bolt":10,"Crushing":8,"Earth":3,"Fire":4,"Necromancy":6,"None":0,"Slashing":7,"Stabbing":5,"Thrown":11,"Water":2}
    
    def test_get_beast_by_weakness_success(self, bestiary, mock_http_adapter):
        expected_response = [
            {"label": "Bladed muspah (150)","value": 19152},
            {"label": "Enraged bladed muspah (250)","value": 28885},
            {"label": "Enraged force muspah (250)","value": 28882},
            {"label": "Enraged throwing muspah (250)","value": 28879},
            {"label": "Force muspah (150)","value": 19151},
            {"label": "Gu ronin (119)","value": 23067},
            {"label": "Gu ronin (119)","value": 23068},
            {"label": "Large bladed muspah (200)","value": 28884},
            {"label": "Large force muspah (200)","value": 28881},
            {"label": "Large throwing muspah (200)","value": 28878},
            {"label": "Throwing muspah (150)","value": 19150},
            {"label": "Vampyre juvinate (84)","value": 22601},
            {"label": "Vampyre juvinate (84)","value": 22602}
        ]
        mock_http_adapter.get.return_value = expected_response
        
        result = bestiary.get_beasts_by_weakness(11)
        
        mock_http_adapter.get.assert_called_once_with(
            base_url=SERVICES_RS,
            path="/m=itemdb_rs/bestiary/weaknessBeasts.json",
            params={"identifier": 11}
        )
        assert isinstance(result, list)
        assert all(isinstance(x, BeastSummary) for x in result)
        assert len(result) == 13
    
    def test_get_beast_by_level_range_success(self, bestiary, mock_http_adapter):
        expected_response = [
            {"value":10532,"label":"Forgotten warrior (141)"},
            {"value":10533,"label":"Forgotten warrior (141)"},
            {"value":10534,"label":"Forgotten warrior (141)"},
            {"value":10535,"label":"Forgotten warrior (141)"},
            {"value":15297,"label":"Ate all the pies (147)"},
            {"value":2025,"label":"Ahrim the Blighted (150)"},
            {"value":2026,"label":"Dharok the Wretched (150)"},
            {"value":2027,"label":"Guthan the Infested (150)"},
            {"value":2028,"label":"Karil the Tainted (150)"},
            {"value":2029,"label":"Torag the Corrupted (150)"},
            {"value":2030,"label":"Verac the Defiled (150)"},
            {"value":19150,"label":"Throwing muspah (150)"},
            {"value":19151,"label":"Force muspah (150)"},
            {"value":19152,"label":"Bladed muspah (150)"}
        ]
        mock_http_adapter.get.return_value = expected_response
        
        result = bestiary.get_beasts_by_level_range(140,150)
        
        mock_http_adapter.get.assert_called_once_with(
            base_url=SERVICES_RS,
            path="/m=itemdb_rs/bestiary/levelGroup.json",
            params={"identifier": "140-150"}
        )
        assert isinstance(result, list)
        assert all(isinstance(x, BeastSummary) for x in result)
        assert len(result) == 14
