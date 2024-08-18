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
    """
    Data class representing a manga.

    Attributes
    ----------
    _client : httpx.Client
        An instance of the HTTP client used for making API requests.
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
    url: str, optional
        The URL to the NewManga vesrion of the manga.
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
    url: str | None = None
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
        """
        Fetches comments for the manga.

        Parameters
        ----------
        sort_by : str, optional
            The sorting method for comments, by default "new".

        Returns
        -------
        CommentsResponse
            The response containing a list of comments.
        """
        params = queries_data.comments.copy()
        params["sort_by"] = sort_by

        response = self._client.get(
            constants.comments.format(slug=self.slug), params=queries_data.comments
        ).json()
        return formatters.json_to_comments_response(response)

    def get_similar(self) -> "SimilarResponse":
        """
        Fetches similar manga recommendations.

        Returns
        -------
        SimilarResponse
            The response containing a list of similar manga.
        """
        response = self._client.get(constants.similar.format(slug=self.slug)).json()
        return formatters.json_to_similar_response(self._client, response)

    def get_chapters(
        self,
        page: int = 1,
        size: int = 25,
        reverse: bool = False,
    ) -> "ChaptersResponse":
        """
        Fetches a paginated list of chapters for the manga.

        Parameters
        ----------
        page : int, optional
            The page number to fetch, by default 1.
        size : int, optional
            The number of chapters per page, by default 25.
        reverse : bool, optional
            If true, chapters are ordered in reverse, by default False.

        Returns
        -------
        ChaptersResponse
            The response containing a list of chapters.
        """
        params = queries_data.chapters.copy()
        params["page"] = str(page)
        params["size"] = str(size)
        params["reverse"] = str(reverse)

        response = self._client.get(
            constants.chapters.format(id=self.id),
            params=params,
        ).json()
        return formatters.json_to_chapters_response(response)
