from typing import Optional
import httpx

from .catalogue import Catalogue
from ..consts import headers


class NewMangaApi:
    def __init__(self, proxy: Optional[str] = None):
        self.client = httpx.Client(
            headers=headers,
            proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}
            if proxy
            else None,
        )
        self.get_catalogue = Catalogue(self.client)
