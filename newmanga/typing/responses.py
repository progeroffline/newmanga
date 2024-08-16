from dataclasses import dataclass
from ..api.manga import Manga


@dataclass()
class CatalogueResponse:
    mangas: list[Manga]
    page: int
    found: int
    total: int
