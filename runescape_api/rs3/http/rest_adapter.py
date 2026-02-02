import requests
from typing import Any, Dict, Optional
from runescape_api.rs3.exceptions import RuneScapeApiException
from runescape_api.rs3.http.base_http_adapter import BaseHttpAdapter

class RestAdapter(BaseHttpAdapter):
    def __init__(self, timeout: int):
        self.timeout = timeout
    
    def get(self, base_url: str, path: str, params: Optional[Dict[str, Any]] = None, raw: bool = False,) -> str | dict:
        full_url = f'{base_url}{path}'
        headers = {'content-type':'application/json'}
        try:
            response = requests.get(
                url=full_url,
                headers=headers,
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            if raw:
                return response
            if not response.content:
                return None
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuneScapeApiException("Request failed") from e