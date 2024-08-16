from dataclasses import dataclass, field
import httpx

from .. import constants, formatters
from ..typing.types import Genre, Tag, Author, Artist, Branch
from ..typing.enums import MangaType, MangaStatus


@dataclass()
class Manga:
    _client: httpx.Client = field(repr=False)
    id: int | None = None
    title_ru: str | None = None
    title_en: str | None = None
    title_original: str | None = None
    image: str | None = None
    type: MangaType | None = None
    rating: float | None = None
    rating_count: int | None = None
    hearts: int | None = None
    views: int | None = None
    bookmarks: int | None = None
    status: MangaStatus | None = None
    description: str | None = None
    genres: list[Genre] = field(default_factory=list)
    tags: list[Tag] = field(default_factory=list)
    author: Author | None = None
    artist: Artist | None = None
    release_date: str | None = None
    adult: str | None = None
    tomes: list[int] = field(default_factory=list)
    count_chapters: int | None = None
    original_status: MangaStatus | None = None
    slug: str | None = None
    branches: list[Branch] = field(default_factory=list)
    original_url: str | None = None
    english_url: str | None = None
    other_url: str | None = None

    def __call__(self, slug: str) -> "Manga":
        response = self._client.get(constants.manga_api + "/" + slug).json()
        return formatters.json_to_manga(self._client, response)
