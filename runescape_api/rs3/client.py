from typing import Optional
from runescape_api.rs3.endpoints.bestiary import Bestiary
from runescape_api.rs3.endpoints.grand_exchange import GrandExchange
from runescape_api.rs3.endpoints.hiscores import Hiscores
from runescape_api.rs3.endpoints.runemetrics import Runemetrics
from runescape_api.rs3.http.rest_adapter import RestAdapter

class RS3Client:
    def __init__(self, timeout: int = 30):
        """
        Entry point for the RuneScape 3 API client.
        """
        self.http_adapter = RestAdapter(timeout=timeout)

        self.bestiary = Bestiary(self.http_adapter)
        self.ge = GrandExchange(self.http_adapter)
        self.hiscores = Hiscores(self.http_adapter)
        self.runemetrics = Runemetrics(self.http_adapter)