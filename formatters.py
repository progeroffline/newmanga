from typing import Any
from . import consts
from .types import Manga, CatalogueResponse, MangaStatus, MangaType


def json_to_manga(data: dict[str, Any]) -> Manga:
    return Manga(
        id=int(data["id"]),
        slug=data["slug"],
        type=MangaType(data["type"]),
        rating=data["rating"],
        rating_rank=data["rating_rank"],
        likes=data["hearts"],
        views=data["views"],
        status=MangaStatus(data["status"]),
        adult=int(data["adult"]),
        tags=data["tags"],
        genres=data["genres"],
        count_chapters=data["count_chapters"],
        title_ru=data["title_ru"],
        title_en=data.get("title_en"),
        title_og=data.get("title_og"),
        image_small=consts.image + "/" + data["image_small"],
        image_large=consts.image + "/" + data["image_large"],
        url=consts.manga + "/" + data["slug"],
        description=data["description"],
        created_at=data["created_at"],
        released_at=data["released_at"],
        released_year=data["released_year"],
        is_active=data["is_active"],
    )


def json_to_catalogue_reponse(data: dict[str, Any]) -> CatalogueResponse:
    return CatalogueResponse(
        page=data["page"],
        found=data["found"],
        total=data["out_of"],
        mangas=[json_to_manga(row["document"]) for row in data["hits"]],
    )
