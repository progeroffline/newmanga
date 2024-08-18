import httpx
from typing import Any
from datetime import datetime

from .manga import MangaFormatter
from ..constants import image_storage_url
from ..api.manga import Manga
from ..typing.types import User, Comment, Chapter


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


def json_to_user(data: dict[str, Any]) -> User:
    """
    Converts a dictionary representing a user to a User object.

    Parameters
    ----------
    data : dict[str, Any]
        A dictionary containing user data.

    Returns
    -------
    User
        An object representing the user.
    """
    return User(
        id=data["id"],
        name=data["name"],
        is_admin=data["is_admin"],
        is_moderator=data["is_moderator"],
        is_translator=data["is_translator"],
        is_active=data["is_active"],
        last_login=datetime.fromisoformat(
            data["last_login"],
        ),
        is_online=data["is_online"],
        image_url=image_storage_url + "/" + data["image"]["name"],
    )


def json_to_comment(data: dict[str, Any]) -> Comment:
    """
    Converts a dictionary representing a comment to a Comment object.

    Parameters
    ----------
    data : dict[str, Any]
        A dictionary containing comment data.

    Returns
    -------
    Comment
        An object representing the comment.
    """
    return Comment(
        id=data["id"],
        text=data["html"],
        chapter_id=data.get("chapter_id"),
        manga_id=data.get("project_id"),
        team_id=data.get("team_id"),
        user=json_to_user(data["user"]),
        created_at=datetime.fromisoformat(data["created_at"]),
        answers=[json_to_comment(answer) for answer in data["children"]],
        likes=data["likes"],
        dislikes=data["dislikes"],
        rating=data["rating"],
        parent_id=data.get("parent_id"),
    )


def json_to_chapter(data: dict[str, Any]) -> Chapter:
    """
    Converts a dictionary representing a chapter to a Chapter object.

    Parameters
    ----------
    data : dict[str, Any]
        A dictionary containing chapter data.

    Returns
    -------
    Chapter
        An object representing the chapter.
    """
    return Chapter(
        id=data["id"],
        tom=data["tom"],
        name=data.get("name"),
        number=int(data["number"]),
        manga_id=data["project_id"],
        branch_id=data["branch_id"],
        hearts=data["hearts"],
        price=data.get("price"),
        translator=data["translator"],
        create_at=datetime.fromisoformat(data["created_at"]),
        pages=data["pages"],
    )
