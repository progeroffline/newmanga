import httpx
from typing import TYPE_CHECKING
from dataclasses import dataclass, field


from .. import constants, formatters, queries_data
from ..typing.types import Genre, Tag, Author, Artist, Branch
from ..typing.enums import MangaType, MangaStatus

if TYPE_CHECKING:
    from ..typing.responses import CommentsResponse, ChaptersResponse, SimilarResponse


@dataclass()
class Manga:
    """Data class representing a manga.

    Parameters
    ----------
    _client : httpx.Client
        An instance of the HTTP client.
    id : int, optional
        The unique identifier for the manga.
    title_ru : str, optional
        The title of the manga in Russian.
    title_en : str, optional
        The title of the manga in English.
    title_original : str, optional
        The original title of the manga.
    image : str, optional
        URL to the manga's cover image.
    type : MangaType, optional
        The type of the manga (e.g., manga, manhua).
    rating : float, optional
        The average rating of the manga.
    rating_count : int, optional
        The number of ratings the manga has received.
    hearts : int, optional
        The number of hearts (likes) the manga has received.
    views : int, optional
        The number of views of the manga.
    bookmarks : int, optional
        The number of bookmarks the manga has received.
    status : MangaStatus, optional
        The publication status of the manga (e.g., ongoing, completed).
    description : str, optional
        A description of the manga.
    genres : list[Genre], optional
        A list of genres associated with the manga.
    tags : list[Tag], optional
        A list of tags associated with the manga.
    author : Author, optional
        The author of the manga.
    artist : Artist, optional
        The artist of the manga.
    release_date : str, optional
        The release date of the manga.
    adult : str, optional
        An indication if the manga is for adults.
    tomes : list[int], optional
        A list of tomes (volumes) of the manga.
    count_chapters : int, optional
        The total number of chapters in the manga.
    original_status : MangaStatus, optional
        The original publication status of the manga.
    slug : str, optional
        A URL-friendly version of the manga's title.
    branches : list[Branch], optional
        A list of branches (e.g., publishers or series) related to the manga.
    original_url : str, optional
        The URL to the original source of the manga.
    english_url : str, optional
        The URL to the English version of the manga.
    other_url : str, optional
        The URL to other versions of the manga.
    """

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
        """
        Fetches and returns a Manga object based on the provided slug.

        Parameters
        ----------
        slug : str
            The URL-friendly title of the manga.

        Returns
        -------
        Manga
            An instance of the Manga class with the data fetched from the API.
        """
        response = self._client.get(constants.manga_api + "/" + slug).json()
        return formatters.json_to_object.json_to_manga(self._client, response)

    def get_comments(self, sort_by: str = "new") -> "CommentsResponse":
        params = queries_data.comments.copy()
        params["sort_by"] = sort_by

        response = self._client.get(
            constants.comments.format(slug=self.slug), params=queries_data.comments
        ).json()
        return formatters.json_to_comments_response(response)

    def get_chapters(self) -> "ChaptersResponse": ...

    def get_similar(self) -> "SimilarResponse": ...
