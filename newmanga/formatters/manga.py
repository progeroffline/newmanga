from datetime import datetime
from typing import Any, Dict, Optional
from ..typing.enums import MangaType, MangaStatus
from ..typing.types import (
    Artist,
    Author,
    Branch,
    Genre,
    Member,
    Tag,
    Translator,
    Team,
    User,
)
from ..constants import image_storage_url


class MangaFormatter:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        self.id: Optional[int] = None
        self.title_ru: Optional[str] = None
        self.title_en: Optional[str] = None
        self.title_original: Optional[str] = None
        self.image: Optional[str] = None
        self.type: Optional[MangaType] = None
        self.rating: Optional[float] = None
        self.rating_count: Optional[int] = None
        self.hearts: Optional[int] = None
        self.views: Optional[int] = None
        self.bookmarks: Optional[int] = None
        self.status: Optional[MangaStatus] = None
        self.description: Optional[str] = None
        self.genres: Optional[list[Genre]] = []
        self.tags: Optional[list[Tag]] = []
        self.author: Optional[Author] = None
        self.artist: Optional[Artist] = None
        self.release_date: Optional[datetime] = None
        self.adult: Optional[int] = None
        self.tomes: Optional[list[int]] = []
        self.count_chapters: Optional[int] = None
        self.original_status: Optional[MangaStatus] = None
        self.slug: Optional[str] = None
        self.branches: Optional[list[Branch]] = []
        self.original_url: Optional[str] = None
        self.english_url: Optional[str] = None
        self.other_url: Optional[str] = None

        self._load_variables()

    def _load_variables(self) -> None:
        self._load_id()
        self._load_title_ru()
        self._load_title_en()
        self._load_title_original()
        self._load_image()
        self._load_type()
        self._load_rating()
        self._load_hearts()
        self._load_views()
        self._load_bookmarks()
        self._load_status()
        self._load_description()
        self._load_genres()
        self._load_tags()
        self._load_author()
        self._load_artist()
        self._load_release_date()
        self._load_adult()
        self._load_tomes()
        self._load_count_chapters()
        self._load_original_status()
        self._load_slug()
        self._load_branches()
        self._load_original_url()
        self._load_english_url()
        self._load_other_url()

    def _load_id(self) -> None:
        self.id = int(self.data["id"]) if self.data.get("id") else None

    def _load_title_ru(self) -> None:
        self.title_ru = (
            self.data["title"]["ru"]
            if self.data.get("title")
            else self.data.get("title_ru")
        )

    def _load_title_en(self) -> None:
        self.title_en = (
            self.data["title"]["en"]
            if self.data.get("title")
            else self.data.get("title_en")
        )

    def _load_title_original(self) -> None:
        self.title_original = (
            self.data["title"]["original"]
            if self.data.get("title")
            else self.data.get("title_original")
        )

    def _load_image(self) -> None:
        self.image = (
            image_storage_url
            + "/"
            + str(
                self.data["image"]["name"]
                if self.data.get("image")
                else self.data.get("image_large")
            )
        )

    def _load_type(self) -> None:
        self.type = MangaType(self.data.get("type"))

    def _load_rating(self) -> None:
        self.rating = self.data.get("rating")

    def _load_hearts(self) -> None:
        self.hearts = self.data.get("hearts")

    def _load_views(self) -> None:
        self.views = self.data.get("views")

    def _load_bookmarks(self) -> None:
        self.bookmarks = self.data.get("bookmarks")

    def _load_status(self) -> None:
        self.status = MangaStatus(self.data.get("status"))

    def _load_description(self) -> None:
        self.description = self.data.get("description")

    def _load_genres(self) -> None:
        if len(self.data["genres"]) == 0:
            return

        if isinstance(self.data["genres"][0], str):
            self.genres = [Genre(title_ru=genre) for genre in self.data["genres"]]
        else:
            self.genres = [
                Genre(
                    id=genre["id"],
                    title_ru=genre["title"]["ru"],
                    title_en=genre["title"]["en"],
                    title_original=genre["title"]["original"],
                )
                for genre in self.data["genres"]
            ]

    def _load_tags(self) -> None:
        if len(self.data["tags"]) == 0:
            return

        if isinstance(self.data["tags"][0], str):
            self.tags = [Tag(title_ru=genre) for genre in self.data["tags"]]
        else:
            self.tags = [
                Tag(
                    id=genre["id"],
                    title_ru=genre["title"]["ru"],
                    title_en=genre["title"]["en"],
                    title_original=genre["title"]["original"],
                )
                for genre in self.data["tags"]
            ]

    def _load_author(self) -> None:
        if self.data.get("author"):
            self.author = Author(
                id=self.data["author"]["id"],
                name=self.data["author"]["name"],
                description=self.data["author"]["description"],
                image_url=image_storage_url
                + "/"
                + self.data["author"]["image"]["name"],
            )

    def _load_artist(self) -> None:
        if self.data.get("author"):
            self.artist = Artist(
                id=self.data["author"]["id"],
                name=self.data["author"]["name"],
                description=self.data["author"]["description"],
                image_url=image_storage_url
                + "/"
                + self.data["author"]["image"]["name"],
            )

    def _load_release_date(self) -> None:
        if self.data.get("released_at"):
            self.release_date = datetime.fromtimestamp(self.data["released_at"])
        else:
            self.release_date = datetime.strptime(self.data["release_date"], "%Y-%m-%d")

    def _load_adult(self) -> None:
        self.adult = int(self.data["adult"]) if self.data.get("adult") else None

    def _load_tomes(self) -> None:
        self.tomes = self.data.get("tomes")

    def _load_count_chapters(self) -> None:
        self.count_chapters = self.data.get("count_chapters")

    def _load_original_status(self) -> None:
        self.original_status = MangaStatus(self.data.get("original_status"))

    def _load_slug(self) -> None:
        self.slug = self.data.get("slug")

    def _load_branches(self) -> None:
        if self.data.get("branches"):
            self.branches = [
                Branch(
                    id=branch["id"],
                    chapters_total=branch["chapters_total"],
                    likes_total=branch["likes_total"],
                    is_default=branch["is_default"],
                    subscription=branch["subscription"],
                    translators=[
                        Translator(
                            id=translator["id"],
                            balance=translator["balance"],
                            is_team=translator["is_team"],
                            is_verified=translator["is_verified"],
                            user=User(
                                id=translator["user"]["id"],
                                name=translator["user"]["name"],
                                is_admin=translator["user"]["is_admin"],
                                is_moderator=translator["user"]["is_moderator"],
                                is_translator=translator["user"]["is_translator"],
                                is_active=translator["user"]["is_active"],
                                last_login=datetime.fromisoformat(
                                    translator["user"]["last_login"],
                                ),
                                is_online=translator["user"]["is_online"],
                                image_url=image_storage_url
                                + "/"
                                + translator["user"]["image"]["name"],
                            )
                            if translator.get("user")
                            else None,
                            team=Team(
                                id=translator["team"]["id"],
                                name=translator["team"]["name"],
                                image_url=image_storage_url
                                + "/"
                                + translator["team"]["image"]["name"],
                                members=[
                                    Member(
                                        id=member["id"],
                                        statuses=member["statuses"],
                                        user=User(
                                            id=member["user"]["id"],
                                            name=member["user"]["name"],
                                            is_admin=member["user"]["is_admin"],
                                            is_moderator=member["user"]["is_moderator"],
                                            is_translator=member["user"][
                                                "is_translator"
                                            ],
                                            is_active=member["user"]["is_active"],
                                            last_login=datetime.fromisoformat(
                                                member["user"]["last_login"],
                                            ),
                                            is_online=member["user"]["is_online"],
                                            image_url=image_storage_url
                                            + "/"
                                            + member["user"]["image"]["name"],
                                        )
                                        if member.get("user")
                                        else None,
                                    )
                                    for member in translator["team"]["members"]
                                ],
                            )
                            if translator.get("team")
                            else None,
                        )
                        for translator in branch["translators"]
                    ],
                )
                for branch in self.data["branches"]
            ]

    def _load_original_url(self) -> None:
        self.original_url = self.data.get("original_url")

    def _load_english_url(self) -> None:
        self.english_url = self.data.get("english_url")

    def _load_other_url(self) -> None:
        self.other_url = self.data.get("other_url")

    def get_vars(self) -> dict[str, Any]:
        vars = self.__dict__
        vars.pop("data")
        if vars.get("created_at"):
            vars.pop("created_at")
        return vars
