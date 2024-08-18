from typing import Any

import httpx
from ..typing.responses import CatalogueResponse, CommentsResponse, SimilarResponse
from . import json_to_object


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
        mangas=[
            json_to_object.json_to_manga(client, row["document"])
            for row in data["hits"]
        ],
    )


def json_to_comments_response(data: list[dict[str, Any]]) -> CommentsResponse:
    return CommentsResponse(
        comments=[json_to_object.json_to_comment(row) for row in data]
    )


def json_to_similar_response(
    client: httpx.Client, data: list[dict[str, Any]]
) -> SimilarResponse:
    return SimilarResponse(
        mangas=[json_to_object.json_to_manga(client, row) for row in data]
    )
