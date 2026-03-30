import pytest
from unittest.mock import Mock
from runescape_api.rs3.constants import SECURE_RS
from runescape_api.rs3.endpoints.hiscores import Hiscores
from runescape_api.rs3.http.base_http_adapter import BaseHttpAdapter
from runescape_api.rs3.models.clan_member import ClanMember
from runescape_api.rs3.models.clan_ranking import ClanRanking
from runescape_api.rs3.models.gim_page import GroupIronmanPage
from runescape_api.rs3.models.group_hiscores_page import GroupHiscoresPage
from runescape_api.rs3.models.hiscores_details import HiscoresDetails
from runescape_api.rs3.models.hiscores_lite import HiscoresLite
from runescape_api.rs3.models.seasonal_ranking import SeasonalRanking
from runescape_api.rs3.models.user_clan_ranking import UserClanRanking

class TestHiscores:

    @pytest.fixture
    def mock_http_adapter(self):
        adapter = Mock(spec=BaseHttpAdapter)
        return adapter
    
    @pytest.fixture
    def hiscores(self, mock_http_adapter):
        hiscores = Hiscores(mock_http_adapter)
        return hiscores
    
    def test_get_ranking_success(self, hiscores, mock_http_adapter):
        expected_response = [
            {
                "name": "Player 1",
                "score": "200,000,000",
                "rank": "1"
            },
            {
                "name": "Player 2",
                "score": "200,000,000",
                "rank": "2"
            }
        ]

        mock_http_adapter.get.return_value = expected_response

        result = hiscores.get_ranking(9,0,2)

        mock_http_adapter.get.assert_called_once_with(
            base_url=SECURE_RS,
            path="/m=hiscore/ranking.json",
            params={"table": 9,"category": 0,"size": 2,},
        )

        assert isinstance(result, list)
        assert len(result) == 2
    
    def test_get_hiscores_lite_success(self, hiscores, mock_http_adapter):
        expected_response = """133806,2927,674925523
        186215,99,14202215
        47611,99,105234580
        200397,99,14046124
        97703,99,59951677
        166961,101,16191859
        134924,99,14983459
        158774,102,18094255
        227193,99,13126527
        211205,99,13392952
        242644,99,13046383
        175166,99,14433261
        163467,100,14461969
        151670,100,14453765
        230872,99,13185103
        225063,99,13264897
        144744,105,25871584
        98905,99,18851266
        118502,103,19612859
        127709,108,32553932
        180537,99,14209924
        122365,100,14437963
        155049,99,13661303
        183119,99,13271814
        131444,99,13945705
        164345,100,15100922
        173396,99,13328550
        137000,116,72279339
        164749,99,13775953
        94843,110,41955383
        -1,0
        -1,0
        -1,0
        -1,0
        -1,1
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,1000
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        21933,102
        -1,0
        -1,0
        101277,11335
        108560,9
        127929,3
        -1,0
        200231,2
        -1,0
        21178,15680
        """

        mock_http_adapter.get.return_value = expected_response

        result = hiscores.get_hiscores_lite("Valid User")

        mock_http_adapter.get.assert_called_once_with(
            base_url=SECURE_RS,
            path="/m=hiscore/index_lite.ws",
            params={"player": "Valid User"},
            raw=True
        )
        
        assert isinstance(result, HiscoresLite)
    
    def test_get_ironman_lite_success(self, hiscores, mock_http_adapter):
        expected_response = """3124,3128,2309565104
        5274,109,35191624
        3331,99,106666717
        10864,100,15345980
        5069,99,105871375
        8641,106,27414217
        5228,99,19177204
        8069,109,37976075
        616,99,104316403
        442,110,156382008
        1327,110,44994567
        754,99,114099452
        692,110,111660211
        1242,110,45146614
        3348,109,36524918
        751,110,130395626
        5097,120,104324374
        1999,99,25958109
        1676,120,200000000
        5424,115,69246495
        4564,120,124529669
        3117,107,29116397
        6562,103,20174536
        2972,99,24129120
        1183,99,38840772
        5594,109,37882847
        2689,99,32705429
        2652,120,200000000
        6608,120,111494365
        1195,120,200000000
        -1,0
        -1,0
        3183,5171143
        -1,0
        -1,1
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        3605,22645
        12709,101
        4100,82
        3203,775
        21654,25
        18595,3
        -1,0
        """

        mock_http_adapter.get.return_value = expected_response

        result = hiscores.get_ironman_lite("Valid Ironman")

        mock_http_adapter.get.assert_called_once_with(
            base_url=SECURE_RS,
            path="/m=hiscore_ironman/index_lite.ws",
            params={"player": "Valid Ironman"},
            raw=True
        )
        
        assert isinstance(result, HiscoresLite)
    
    def test_get_hardcore_ironman_lite_success(self, hiscores, mock_http_adapter):
        expected_response = """3124,3128,2309565104
        5274,109,35191624
        3331,99,106666717
        10864,100,15345980
        5069,99,105871375
        8641,106,27414217
        5228,99,19177204
        8069,109,37976075
        616,99,104316403
        442,110,156382008
        1327,110,44994567
        754,99,114099452
        692,110,111660211
        1242,110,45146614
        3348,109,36524918
        751,110,130395626
        5097,120,104324374
        1999,99,25958109
        1676,120,200000000
        5424,115,69246495
        4564,120,124529669
        3117,107,29116397
        6562,103,20174536
        2972,99,24129120
        1183,99,38840772
        5594,109,37882847
        2689,99,32705429
        2652,120,200000000
        6608,120,111494365
        1195,120,200000000
        -1,0
        -1,0
        3183,5171143
        -1,0
        -1,1
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        -1,0
        3605,22645
        12709,101
        4100,82
        3203,775
        21654,25
        18595,3
        -1,0
        """

        mock_http_adapter.get.return_value = expected_response

        result = hiscores.get_hardcore_ironman_lite("Valid Hardcore Ironman")

        mock_http_adapter.get.assert_called_once_with(
            base_url=SECURE_RS,
            path="/m=hiscore_hardcore_ironman/index_lite.ws",
            params={"player": "Valid Hardcore Ironman"},
            raw=True
        )
        
        assert isinstance(result, HiscoresLite)
    
    def test_get_leagues_lite_success(self, hiscores, mock_http_adapter):
        expected_response = """37519,2240,332200006
        25598,99,13516375
        31643,99,13537002
        25823,99,13509346
        34713,99,14018877
        39908,64,408486
        31136,99,13408227
        37816,76,1433431
        25205,83,2746694
        38493,78,1637692
        46249,65,460698
        34594,76,1403152
        31685,79,1873389
        45436,81,2209495
        51146,81,2403711
        50053,91,6174183
        53161,51,113982
        6116,99,30343747
        52248,54,153043
        36426,90,5583359
        51575,70,759867
        50868,53,136606
        48513,48,91044
        54169,64,446830
        27484,71,890047
        47965,46,70442
        25426,86,3955480
        34925,120,200000000
        53349,48,91504
        32356,71,823297
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        38781,3235
        51228,2
        -1,-1
        -1,-1
        -1,-1
        -1,-1
        39767,15680
        """

        mock_http_adapter.get.return_value = expected_response

        result = hiscores.get_leagues_lite("Valid Leagues")

        mock_http_adapter.get.assert_called_once_with(
            base_url=SECURE_RS,
            path="/m=hiscore_leagues/index_lite.ws",
            params={"player": "Valid Leagues"},
            raw=True
        )
        
        assert isinstance(result, HiscoresLite)
    
    def test_get_seasonal_ranking_success(self, hiscores, mock_http_adapter):
        expected_response = [
            {
                "score_raw": 112200,
                "endDate": "10 Sep 2017",
                "score_formatted": "00:01:52",
                "rank": 3846,
                "hiscoreId": 1504002637056,
                "title": "Fastest kill time: Queen Black Dragon",
                "startDate": "04 Sep 2017"
            },
            {
                "score_raw": 569382,
                "endDate": "21 Jul 2015",
                "score_formatted": "569,382",
                "rank": 43178,
                "hiscoreId": 1435566966734,
                "title": "Life Points Healed",
                "startDate": "15 Jul 2015"
            },
            {
                "score_raw": 3,
                "endDate": "10 Jan 2015",
                "score_formatted": "3",
                "rank": 30724,
                "hiscoreId": 1420329600006,
                "title": "Deaths",
                "startDate": "04 Jan 2015"
            },
            {
                "score_raw": 718471,
                "endDate": "10 May 2014",
                "score_formatted": "718,471",
                "rank": 21394,
                "hiscoreId": 1399244400005,
                "title": "Life Points Healed",
                "startDate": "04 May 2014"
            },
            {
                "score_raw": 630871,
                "endDate": "03 May 2014",
                "score_formatted": "630,871",
                "rank": 28633,
                "hiscoreId": 1398639600050,
                "title": "Life Points Healed",
                "startDate": "27 Apr 2014"
            },
            {
                "score_raw": 403,
                "endDate": "03 May 2014",
                "score_formatted": "403",
                "rank": 14817,
                "hiscoreId": 1398034800005,
                "title": "Slayer Tower Kills",
                "startDate": "20 Apr 2014"
            },
            {
                "score_raw": 10,
                "endDate": "10 Nov 2013",
                "score_formatted": "10",
                "rank": 34035,
                "hiscoreId": 1382922000018,
                "title": "Chronicle Fragments Offered",
                "startDate": "28 Oct 2013"
            }
        ]

        mock_http_adapter.get.return_value = expected_response

        result = hiscores.get_seasonal_ranking("Valid User", True)

        mock_http_adapter.get.assert_called_once_with(
            base_url=SECURE_RS,
            path="/m=temp-hiscores/getRankings.json",
            params={"player": "Valid User", "status": "archived"}
        )
        
        assert isinstance(result, list)
        assert all(isinstance(x, SeasonalRanking) for x in result)
        assert len(result) == 7
    
    def test_get_hiscores_details_success(self, hiscores, mock_http_adapter):
        expected_response = [
            {
                "status": "ARCHIVED",
                "name": "temp_hiscore_zombiescape_2017_october_finale_mk3",
                "id": 1510570900743,
                "recurrence": 0,
                "startDate": "18 Nov 2017",
                "endDate": "18 Nov 2017",
                "type": "LONG",
                "title": "Dimension of the Damned Finale October 2017 Score",
                "description": "The players score during the finale.",
                "daysRunning": 1,
                "monthsRunning": 0
            },
            {
                "status": "ARCHIVED",
                "name": "temp_hiscore_2017_araxxi_kill_time",
                "id": 1508716800048,
                "recurrence": 7,
                "startDate": "23 Oct 2017",
                "endDate": "29 Oct 2017",
                "type": "TIME",
                "title": "Fastest kill time: Araxxi (Solo)",
                "description": "The fastest kill times for Araxxi (Solo).",
                "daysRunning": 7,
                "monthsRunning": 0
            }
        ]

        mock_http_adapter.get.return_value = expected_response

        result = hiscores.get_hiscores_details(True)

        mock_http_adapter.get.assert_called_once_with(
            base_url=SECURE_RS,
            path="/m=temp-hiscores/getHiscoreDetails.json",
            params={"status": "archived"}
        )
        
        assert isinstance(result, list)
        assert all(isinstance(x, HiscoresDetails) for x in result)
        assert len(result) == 2
    
    def test_get_clan_ranking_success(self, hiscores, mock_http_adapter):
        expected_response = [
            {
                "rank": 1,
                "clan_name": "Clan 1",
                "clan_mates": 500,
                "xp_total": 1346665431166
            },
            {
                "rank": 2,
                "clan_name": "Clan 2",
                "clan_mates": 500,
                "xp_total": 1157075088930
            },
            {
                "rank": 3,
                "clan_name": "Clan 3",
                "clan_mates": 497,
                "xp_total": 798759354626
            }
        ]

        mock_http_adapter.get.return_value = expected_response

        result = hiscores.get_clan_ranking()

        mock_http_adapter.get.assert_called_once_with(
            base_url=SECURE_RS,
            path="/m=clan-hiscores/clanRanking.json"
        )
        
        assert isinstance(result, list)
        assert all(isinstance(x, ClanRanking) for x in result)
        assert len(result) == 3
    
    def test_get_user_clan_ranking_success(self, hiscores, mock_http_adapter):
        expected_response = {
            "displayName": "Player Name",
            "clanName": "Clan Name",
            "clanRank": 1
        }

        mock_http_adapter.get.return_value = expected_response

        result = hiscores.get_user_clan_ranking(0)

        mock_http_adapter.get.assert_called_once_with(
            base_url=SECURE_RS,
            path="/c=0/m=clan-hiscores/userClanRanking.json"
        )
        
        assert isinstance(result, UserClanRanking)
    
    def test_get_clan_members_lite_success(self, hiscores, mock_http_adapter):
        expected_response = """Clanmate, Clan Rank, Total XP, Kills
        Clan Owner,Owner,5502522298,9
        Clan Deputy Owner,Deputy Owner,4746568967,1
        Clan Coordinator,Coordinator,2022738534,0
        Clan Organiser,Organiser,2288142902,0
        Clan Admin,Admin,1228413586,0"""

        mock_response = Mock()
        mock_response.text = expected_response
        mock_http_adapter.get.return_value = mock_response

        result = hiscores.get_clan_members_lite("Clan Name")

        mock_http_adapter.get.assert_called_once_with(
            base_url=SECURE_RS,
            path="/m=clan-hiscores/members_lite.ws",
            params={"clanName": "Clan Name"},
            raw=True
        )
        
        assert isinstance(result, list)
        assert all(isinstance(x, ClanMember) for x in result)
        assert len(result) == 5
    
    def test_get_bosses_groups_success(self, hiscores, mock_http_adapter):
        expected_response = {
            "content": [
                {
                    "id": 167572,
                    "bossId": 1,
                    "size": 2,
                    "rank": 1,
                    "enrage": 60000,
                    "killTimeSeconds": 470.40002,
                    "timeOfKill": 1757344034,
                    "members": [
                        { "name": "Member 1" },
                        { "name": "Member 2" }
                    ]
                }
            ],
            "totalElements": 92065,
            "totalPages": 92065,
            "first": True,
            "last": False,
            "numberOfElements": 1,
            "number": 0,
            "size": 1,
            "empty": False
        }

        mock_http_adapter.get.return_value = expected_response

        result = hiscores.get_bosses_groups(2,1,1,0)

        mock_http_adapter.get.assert_called_once_with(
            base_url=SECURE_RS,
            path="/m=group_hiscores/v1//groups",
            params={"groupSize": 2,"size": 1,"bossId": 1,"page": 0}
        )
        
        assert isinstance(result, GroupHiscoresPage)

    def test_get_group_ironman_success(self, hiscores, mock_http_adapter):
        expected_response = {
            "totalElements": 4160,
            "totalPages": 1387,
            "size": 3,
            "content": [
                {
                    "id": 403056,
                    "name": "any+spotters",
                    "groupTotalXp": 7161644378,
                    "groupTotalLevel": 6422,
                    "size": 2,
                    "toHighlight": False,
                    "isCompetitive": True,
                    "founder": True
                },
                {
                    "id": 409285,
                    "name": "venus+core",
                    "groupTotalXp": 7106936505,
                    "groupTotalLevel": 6415,
                    "size": 2,
                    "toHighlight": False,
                    "isCompetitive": True,
                    "founder": True
                },
                {
                    "id": 403073,
                    "name": "trihard",
                    "groupTotalXp": 6688537929,
                    "groupTotalLevel": 6330,
                    "size": 2,
                    "toHighlight": False,
                    "isCompetitive": True,
                    "founder": True
                }
            ],
            "first": True,
            "last": False,
            "numberOfElements": 3,
            "pageNumber": 0,
            "empty": False
        }

        mock_http_adapter.get.return_value = expected_response

        result = hiscores.get_group_ironman(2,3,0,True)

        mock_http_adapter.get.assert_called_once_with(
            base_url=SECURE_RS,
            path="/m=runescape_gim_hiscores//v1/groupScores",
            params={"groupSize": 2,"size": 3,"page": 0,"isCompetitive": True}
        )
        
        assert isinstance(result, GroupIronmanPage)

    def test_get_group_ironman_invalid_type(self, hiscores):
        with pytest.raises(TypeError):
            hiscores.get_group_ironman(2,3,0,1)
