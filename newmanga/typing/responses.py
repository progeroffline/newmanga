from dataclasses import dataclass

from ..api.manga import Manga
from .types import Comment, Chapter


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
    """
    Data class representing a response containing a list of comments.

    Attributes
    ----------
    comments : list[Comment]
        A list of comments.
    """

    comments: list[Comment]


@dataclass()
class SimilarResponse:
    """
    Data class representing a response containing a list of similar mangas.

    Attributes
    ----------
    mangas : list[Manga]
        A list of similar mangas.
    """

    mangas: list[Manga]


@dataclass()
class ChaptersResponse:
    """
    Data class representing a response containing a list of chapters and the total count.

    Attributes
    ----------
    chapters : list[Chapter]
        A list of chapters.
    count : int
        The total number of chapters available.
    """

    chapters: list[Chapter]
    count: int
