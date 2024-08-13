from dataclasses import dataclass
from typing import Optional
from enum import Enum


class MangaStatus(Enum):
    ON_GOING = "on_going"
    ABANDONED = "abandoned"
    COMPLETED = "completed"


class MangaType(Enum):
    MANHYA = "manhya"
    MANHWA = "manhwa"
    MANGA = "manga"
    RUSSIAN = "russian"
    COMICS = "comics"
    SINGLE = "single"
    OEL = "oel"


@dataclass()
class Manga:
    id: int
    slug: str
    type: MangaType

    rating: float
    rating_rank: float
    likes: int
    views: int

    status: MangaStatus
    adult: int
    tags: list[str]
    genres: list[str]
    count_chapters: int

    title_ru: str
    title_en: Optional[str]
    title_og: Optional[str]

    image_small: str
    image_large: str
    url: str

    description: str

    created_at: int
    released_at: int
    released_year: int
    is_active: bool


@dataclass()
class CatalogueResponse:
    mangas: list[Manga]
    page: int
    found: int
    total: int
