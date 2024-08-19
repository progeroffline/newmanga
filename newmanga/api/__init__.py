from typing import Optional
import httpx

from .tags import Tags
from .updates import Updates
from .read_now import ReadNow
from .popular import Popular
from .catalogue import Catalogue
from .manga import Manga
from ..constants import headers


class NewMangaApi:
    def __init__(self, proxy: Optional[str] = None):
        self.client = httpx.Client(
            headers=headers,
            proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}
            if proxy
            else None,
        )
        self.get_catalogue = Catalogue(self.client)
        self.get_popular = Popular(self.client)
        self.get_read_now = ReadNow(self.client)
        self.get_updates = Updates(self.client)
        self.get_tags = Tags(self.client)
        self.get_manga = Manga(self.client)
