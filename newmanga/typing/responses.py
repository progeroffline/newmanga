from dataclasses import dataclass

from ..api.manga import Manga
from .types import Comment


@dataclass()
class CatalogueResponse:
    """Response object for a catalogue query.

    Attributes
    ----------
    mangas : list[Manga]
        A list of `Manga` objects representing the manga in the catalogue.
    page : int
        The current page number of the catalogue response.
    found : int
        The total number of manga found that match the query.
    total : int
        The total number of manga available in the catalogue.
    """

    mangas: list[Manga]
    page: int
    found: int
    total: int


@dataclass()
class CommentsResponse:
    comments: list[Comment]


@dataclass()
class ChaptersResponse: ...


@dataclass()
class SimilarResponse: ...
