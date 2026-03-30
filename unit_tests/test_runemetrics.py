import pytest
from unittest.mock import Mock
from runescape_api.rs3.constants import APPS_RS
from runescape_api.rs3.endpoints.runemetrics import Runemetrics
from runescape_api.rs3.exceptions import RunemetricsProfileError
from runescape_api.rs3.http.base_http_adapter import BaseHttpAdapter
from runescape_api.rs3.models.monthly_xp import MonthlyXp
from runescape_api.rs3.models.quest import Quest
from runescape_api.rs3.models.runemetrics_profile import RunemetricsProfile

class TestRunemetrics:

    @pytest.fixture
    def mock_http_adapter(self):
        adapter = Mock(spec=BaseHttpAdapter)
        return adapter
    
    @pytest.fixture
    def runemetrics(self, mock_http_adapter):
        runemetrics = Runemetrics(mock_http_adapter)
        return runemetrics
    
    def test_profile_success(self, runemetrics, mock_http_adapter):
        mock_http_adapter.get.return_value = {
            "magic": 14983459,
            "questsstarted": 4,
            "totalskill": 2927,
            "questscomplete": 234,
            "questsnotstarted": 122,
            "totalxp": 674925523,
            "ranged": 59951677,
            "activities": [
                {
                    "date": "24-Mar-2026 21:30",
                    "details": "I received a vision calling me to the ancient and beautiful land of Havenhythe, and helped the villagers of Wendlewick construct a lodestone.",
                    "text": "Quest complete: Visions of Havenhythe"
                }
            ],
            "skillvalues": [
                {"level": 99,"xp": 1052345808,"rank": 47636,"id": 1},
                {"level": 116,"xp": 722793397,"rank": 137046,"id": 26},
                {"level": 99,"xp": 599516773,"rank": 97755,"id": 3},
                {"level": 110,"xp": 419553832,"rank": 94862,"id": 28},
                {"level": 108,"xp": 325539321,"rank": 127764,"id": 18},
                {"level": 105,"xp": 258715848,"rank": 144814,"id": 15},
                {"level": 103,"xp": 196128597,"rank": 118479,"id": 17},
                {"level": 99,"xp": 188512661,"rank": 98933,"id": 16},
                {"level": 102,"xp": 180942551,"rank": 158874,"id": 6},
                {"level": 101,"xp": 161918598,"rank": 167074,"id": 4},
                {"level": 100,"xp": 151009220,"rank": 164439,"id": 24},
                {"level": 99,"xp": 149834590,"rank": 135011,"id": 5},
                {"level": 100,"xp": 144619696,"rank": 163550,"id": 11},
                {"level": 100,"xp": 144537656,"rank": 151736,"id": 12},
                {"level": 100,"xp": 144379630,"rank": 122441,"id": 20},
                {"level": 99,"xp": 144332619,"rank": 175273,"id": 10},
                {"level": 99,"xp": 142099244,"rank": 180614,"id": 19},
                {"level": 99,"xp": 142022156,"rank": 186316,"id": 0},
                {"level": 99,"xp": 140461244,"rank": 200531,"id": 2},
                {"level": 99,"xp": 139457054,"rank": 131522,"id": 23},
                {"level": 99,"xp": 137759539,"rank": 164826,"id": 27},
                {"level": 99,"xp": 136613032,"rank": 155092,"id": 21},
                {"level": 99,"xp": 133929520,"rank": 211335,"id": 8},
                {"level": 99,"xp": 133285507,"rank": 173494,"id": 25},
                {"level": 99,"xp": 132718147,"rank": 183229,"id": 22},
                {"level": 99,"xp": 132648973,"rank": 225203,"id": 14},
                {"level": 99,"xp": 131851032,"rank": 231012,"id": 13},
                {"level": 99,"xp": 131265279,"rank": 227345,"id": 7},
                {"level": 99,"xp": 130463833,"rank": 242808,"id": 9}
            ],
            "name": "Valid User",
            "rank": "133,859",
            "melee": 390080051,
            "combatlevel": 145,
            "loggedIn": "false"
        }

        result = runemetrics.get_profile("Valid User",1)

        mock_http_adapter.get.assert_called_once()
        assert isinstance(result, RunemetricsProfile)
    
    def test_profile_private(self, runemetrics, mock_http_adapter):
        mock_http_adapter.get.return_value = {
            "error": "PROFILE_PRIVATE",
            "loggedIn": "false"
        }

        with pytest.raises(RunemetricsProfileError):
            runemetrics.get_profile("Invalid User", 1)
    
    def test_get_quests_success(self, runemetrics, mock_http_adapter):
        expected_response = {
            "quests": [
                {"title": "A Fairy Tale I - Growing Pains","status": "COMPLETED","difficulty": 2,"members": True,"questPoints": 2,"userEligible": True},
                {"title": "A Shadow over Ashdale","status": "COMPLETED","difficulty": 0,"members": False,"questPoints": 1,"userEligible": True},
                {"title": "'Phite Club","status": "NOT_STARTED","difficulty": 3,"members": True,"questPoints": 1,"userEligible": False},
                {"title": "A Void Dance","status": "NOT_STARTED","difficulty": 2,"members": True,"questPoints": 1,"userEligible": True},
            ],
            "loggedIn": "false"
        }

        mock_http_adapter.get.return_value = expected_response

        result = runemetrics.get_quests("Valid User")

        mock_http_adapter.get.assert_called_once_with(
            base_url=APPS_RS,
            path="/runemetrics/quests",
            params={"user": "Valid User"},
        )

        assert isinstance(result, list)
        assert all(isinstance(x, Quest) for x in result)
        assert len(result) == 4