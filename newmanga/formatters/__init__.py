from typing import Any

import httpx
from ..typing.responses import CatalogueResponse
from ..api.manga import Manga
from .manga import MangaFormatter


def json_to_manga(client: httpx.Client, data: dict[str, Any]) -> Manga:
    return Manga(_client=client, **MangaFormatter(data).get_vars())


def json_to_catalogue_reponse(
    client: httpx.Client, data: dict[str, Any]
) -> CatalogueResponse:
    return CatalogueResponse(
        page=data["page"],
        found=data["found"],
        total=data["out_of"],
        mangas=[json_to_manga(client, row["document"]) for row in data["hits"]],
    )
