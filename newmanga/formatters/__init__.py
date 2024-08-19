from typing import Any

import httpx
from ..typing.responses import (
    CatalogueResponse,
    ChaptersResponse,
    CommentsResponse,
    PopularResponse,
    ReadNowResponse,
    SimilarResponse,
    TagsResponse,
    UpdatesResponse,
)
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


def json_to_popular_response(
    client: httpx.Client,
    data: dict[str, Any],
    page: int,
) -> PopularResponse:
    """
    Convert JSON data to a PopularResponse object.

    Parameters
    ----------
    client : httpx.Client
        An instance of the HTTP client.
    data : dict[str, Any]
        The JSON data containing popular manga information.
    page : int
        The current page number.

    Returns
    -------
    PopularResponse
        A PopularResponse object containing the parsed data.
    """
    return PopularResponse(
        page=page,
        total=data["count"],
        mangas=[json_to_object.json_to_manga(client, row) for row in data["items"]],
    )


def json_to_read_now_response(
    client: httpx.Client,
    data: list[dict[str, Any]],
) -> ReadNowResponse:
    """
    Convert JSON data to a ReadNowResponse object.

    Parameters
    ----------
    client : httpx.Client
        An instance of the HTTP client.
    data : list[dict[str, Any]]
        The JSON data containing 'Read Now' manga information.

    Returns
    -------
    ReadNowResponse
        A ReadNowResponse object containing the parsed data.
    """
    return ReadNowResponse(
        total=len(data),
        mangas=[json_to_object.json_to_manga(client, row) for row in data],
    )


def json_to_updates_response(
    client: httpx.Client,
    data: dict[str, Any],
    page: int,
) -> UpdatesResponse:
    """
    Convert JSON data to an UpdatesResponse object.

    Parameters
    ----------
    client : httpx.Client
        An instance of the HTTP client.
    data : dict[str, Any]
        The JSON data containing manga updates information.
    page : int
        The current page number.

    Returns
    -------
    UpdatesResponse
        An UpdatesResponse object containing the parsed data.
    """
    return UpdatesResponse(
        page=page,
        total=data["count"],
        mangas=[json_to_object.json_to_manga(client, row) for row in data["items"]],
    )


def json_to_tags_response(
    data: list[dict[str, Any]],
) -> TagsResponse:
    """
    Convert JSON data to a TagsResponse object.

    Parameters
    ----------
    data : list[dict[str, Any]]
        The JSON data containing tags information.

    Returns
    -------
    TagsResponse
        A TagsResponse object containing the parsed and sorted tags data.
    """
    tags = [json_to_object.json_to_tag(row) for row in data]
    tags.sort(key=lambda tag: tag.id if tag.id else 0)
    return TagsResponse(tags=tags, total=len(data))


def json_to_comments_response(data: list[dict[str, Any]]) -> CommentsResponse:
    """
    Converts a list of dictionaries representing comments to a CommentsResponse object.

    Parameters
    ----------
    data : list[dict[str, Any]]
        A list of dictionaries, each representing a comment.

    Returns
    -------
    CommentsResponse
        An object containing the list of comments.
    """
    return CommentsResponse(
        comments=[json_to_object.json_to_comment(row) for row in data]
    )


def json_to_similar_response(
    client: httpx.Client, data: list[dict[str, Any]]
) -> SimilarResponse:
    """
    Converts a list of dictionaries representing similar manga to a SimilarResponse object.

    Parameters
    ----------
    client : httpx.Client
        An instance of the HTTP client.
    data : list[dict[str, Any]]
        A list of dictionaries, each representing a similar manga.

    Returns
    -------
    SimilarResponse
        An object containing the list of similar manga.
    """
    return SimilarResponse(
        mangas=[json_to_object.json_to_manga(client, row) for row in data]
    )


def json_to_chapters_response(data: dict[str, Any]) -> ChaptersResponse:
    """
    Converts a dictionary representing chapters to a ChaptersResponse object.

    Parameters
    ----------
    data : dict[str, Any]
        A dictionary containing the count of chapters and a list of chapter items.

    Returns
    -------
    ChaptersResponse
        An object containing the chapter count and list of chapters.
    """
    return ChaptersResponse(
        count=data["count"],
        chapters=[json_to_object.json_to_chapter(row) for row in data["items"]],
    )
