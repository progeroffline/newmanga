from dataclasses import dataclass

from ..api.manga import Manga
from .types import Comment, Chapter, Tag


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
class PopularResponse:
    """
    Represents a response containing popular manga information.

    Parameters
    ----------
    mangas : List[Manga]
        A list of Manga objects representing popular manga.
    total : int
        The total number of popular manga available.
    page : int
        The current page number of the response.

    Attributes
    ----------
    mangas : List[Manga]
        A list of Manga objects representing popular manga.
    total : int
        The total number of popular manga available.
    page : int
        The current page number of the response.
    """

    mangas: list[Manga]
    total: int
    page: int


@dataclass()
class ReadNowResponse:
    """
    Represents a response containing 'Read Now' manga information.

    Parameters
    ----------
    mangas : List[Manga]
        A list of Manga objects representing 'Read Now' manga.
    total : int
        The total number of 'Read Now' manga available.

    Attributes
    ----------
    mangas : List[Manga]
        A list of Manga objects representing 'Read Now' manga.
    total : int
        The total number of 'Read Now' manga available.
    """

    mangas: list[Manga]
    total: int


@dataclass()
class UpdatesResponse:
    """
    Represents a response containing manga updates information.

    Parameters
    ----------
    mangas : List[Manga]
        A list of Manga objects representing updated manga.
    total : int
        The total number of updated manga available.
    page : int
        The current page number of the response.

    Attributes
    ----------
    mangas : List[Manga]
        A list of Manga objects representing updated manga.
    total : int
        The total number of updated manga available.
    page : int
        The current page number of the response.
    """

    mangas: list[Manga]
    total: int
    page: int


@dataclass()
class TagsResponse:
    """
    Represents a response containing tags information.

    Parameters
    ----------
    tags : List[Tag]
        A list of Tag objects.
    total : int
        The total number of tags available.

    Attributes
    ----------
    tags : List[Tag]
        A list of Tag objects.
    total : int
        The total number of tags available.
    """

    tags: list[Tag]
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
