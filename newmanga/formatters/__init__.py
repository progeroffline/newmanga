from typing import Any

import httpx
from ..typing.responses import CatalogueResponse
from ..api.manga import Manga
from .manga import MangaFormatter


def json_to_manga(client: httpx.Client, data: dict[str, Any]) -> Manga:
    """
    Convert JSON data to a Manga object.

    Parameters
    ----------
    client : httpx.Client
        An instance of the HTTP client.
    data : dict[str, Any]
        A dictionary containing manga data.

    Returns
    -------
    Manga
        An instance of the Manga class initialized with the data from the dictionary.
    """
    return Manga(_client=client, **MangaFormatter(data).get_vars())


def json_to_catalogue_reponse(
    client: httpx.Client, data: dict[str, Any]
) -> CatalogueResponse:
    """
    Convert JSON data to a CatalogueResponse object.

    Parameters
    ----------
    client : httpx.Client
        An instance of the HTTP client.
    data : dict[str, Any]
        A dictionary containing catalogue data.

    Returns
    -------
    CatalogueResponse
        An instance of the CatalogueResponse class initialized with the data from the dictionary.
    """
    return CatalogueResponse(
        page=data["page"],
        found=data["found"],
        total=data["out_of"],
        mangas=[json_to_manga(client, row["document"]) for row in data["hits"]],
    )
