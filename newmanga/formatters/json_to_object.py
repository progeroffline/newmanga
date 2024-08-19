import httpx
from typing import Any
from datetime import datetime
from .manga import MangaFormatter
from ..constants import image_storage_url
from ..api.manga import Manga
from ..typing.types import Tag, User, Comment, Chapter


def json_to_manga(client: httpx.Client, data: dict[str, Any]) -> Manga:
    """
    Convert JSON data to a Manga object.

    Parameters
    ----------
    client : httpx.Client
        An instance of the HTTP client used for making API requests.
    data : dict[str, Any]
        A dictionary containing manga data with various attributes.

    Returns
    -------
    Manga
        A Manga object initialized with the data from the input dictionary,
        containing attributes such as title, description, chapters, etc.
    """
    return Manga(_client=client, **MangaFormatter(data).get_vars())


def json_to_user(data: dict[str, Any]) -> User:
    """
    Convert JSON data to a User object.

    Parameters
    ----------
    data : dict[str, Any]
        A dictionary containing user information with the following keys:
        - 'id': The user's unique identifier
        - 'name': The user's name
        - 'is_admin': Boolean indicating admin status
        - 'is_moderator': Boolean indicating moderator status
        - 'is_translator': Boolean indicating translator status
        - 'is_active': Boolean indicating if the user is active
        - 'last_login': ISO format string of last login time
        - 'is_online': Boolean indicating if the user is currently online
        - 'image': A dictionary containing 'name' key for the user's image

    Returns
    -------
    User
        A User object containing the parsed data with attributes corresponding
        to the input dictionary keys.
    """
    return User(
        id=data["id"],
        name=data["name"],
        is_admin=data["is_admin"],
        is_moderator=data["is_moderator"],
        is_translator=data["is_translator"],
        is_active=data["is_active"],
        last_login=datetime.fromisoformat(data["last_login"]),
        is_online=data["is_online"],
        image_url=image_storage_url + "/" + data["image"]["name"],
    )


def json_to_comment(data: dict[str, Any]) -> Comment:
    """
    Convert JSON data to a Comment object.

    Parameters
    ----------
    data : dict[str, Any]
        A dictionary containing comment information with the following keys:
        - 'id': The comment's unique identifier
        - 'html': The comment's text content
        - 'chapter_id': ID of the associated chapter (optional)
        - 'project_id': ID of the associated manga project (optional)
        - 'team_id': ID of the associated team (optional)
        - 'user': A dictionary containing user data
        - 'created_at': ISO format string of comment creation time
        - 'children': A list of dictionaries representing reply comments
        - 'likes': Number of likes
        - 'dislikes': Number of dislikes
        - 'rating': The comment's rating
        - 'parent_id': ID of the parent comment (optional)

    Returns
    -------
    Comment
        A Comment object containing the parsed data with attributes corresponding
        to the input dictionary keys.
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
    Convert JSON data to a Chapter object.

    Parameters
    ----------
    data : dict[str, Any]
        A dictionary containing chapter information with the following keys:
        - 'id': The chapter's unique identifier
        - 'tom': The volume number
        - 'name': The chapter's name (optional)
        - 'number': The chapter number
        - 'project_id': ID of the associated manga project
        - 'branch_id': ID of the associated branch
        - 'hearts': Number of hearts/likes
        - 'price': The chapter's price (optional)
        - 'translator': Information about the translator
        - 'created_at': ISO format string of chapter creation time
        - 'pages': Number of pages in the chapter

    Returns
    -------
    Chapter
        A Chapter object containing the parsed data with attributes corresponding
        to the input dictionary keys.
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


def json_to_tag(data: dict[str, Any]) -> Tag:
    """
    Convert JSON data to a Tag object.

    Parameters
    ----------
    data : dict[str, Any]
        A dictionary containing tag information with the following keys:
        - 'id': The tag's identifier
        - 'title': A nested dictionary with language-specific titles
            - 'ru': Russian title
            - 'en': English title
            - 'original': Original language title

    Returns
    -------
    Tag
        A Tag object containing the parsed data with the following attributes:
        - id: The tag's identifier
        - title_ru: Russian title
        - title_en: English title
        - title_original: Original language title
    """
    return Tag(
        id=data["id"],
        title_ru=data["title"]["ru"],
        title_en=data["title"]["en"],
        title_original=data["title"]["original"],
    )
