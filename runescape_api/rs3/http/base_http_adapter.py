from abc import ABC, abstractmethod
from typing import Any, Dict, Optional

class BaseHttpAdapter(ABC):
    @abstractmethod
    def get(self, base_url: str, path: str, params: Optional[Dict[str, Any]] = None, raw: bool = False) -> dict:
        pass