from dataclasses import dataclass
from datetime import datetime
from typing import Any, List, Optional


@dataclass()
class Genre:
    """Represents a genre associated with a manga.

    Attributes
    ----------
    id : Optional[int]
        The unique identifier for the genre.
    title_en : Optional[str]
        The English title of the genre.
    title_ru : Optional[str]
        The Russian title of the genre.
    title_original : Optional[str]
        The original title of the genre.
    """

    id: Optional[int] = None
    title_en: Optional[str] = None
    title_ru: Optional[str] = None
    title_original: Optional[str] = None


@dataclass()
class Tag:
    """Represents a tag associated with a manga.

    Attributes
    ----------
    id : Optional[int]
        The unique identifier for the tag.
    title_en : Optional[str]
        The English title of the tag.
    title_ru : Optional[str]
        The Russian title of the tag.
    title_original : Optional[str]
        The original title of the tag.
    """

    id: Optional[int] = None
    title_en: Optional[str] = None
    title_ru: Optional[str] = None
    title_original: Optional[str] = None


@dataclass()
class User:
    """Represents a user who can be part of a team or a translator.

    Attributes
    ----------
    id : int
        The unique identifier for the user.
    name : str
        The name of the user.
    is_admin : bool
        Indicates if the user is an admin.
    is_moderator : bool
        Indicates if the user is a moderator.
    is_translator : bool
        Indicates if the user is a translator.
    is_active : bool
        Indicates if the user is active.
    last_login : datetime
        The last login timestamp of the user.
    is_online : bool
        Indicates if the user is currently online.
    image_url : str
        The URL of the user's profile image.
    """

    id: int
    name: str
    is_admin: bool
    is_moderator: bool
    is_translator: bool
    is_active: bool
    last_login: datetime
    is_online: bool
    image_url: str


@dataclass()
class Member:
    """Represents a member of a team.

    Attributes
    ----------
    id : int
        The unique identifier for the member.
    user : Optional[User]
        The user associated with the member.
    statuses : List[str]
        A list of statuses for the member.
    """

    id: int
    user: Optional[User]
    statuses: List[str]


@dataclass()
class Team:
    """Represents a team of translators.

    Attributes
    ----------
    id : int
        The unique identifier for the team.
    name : str
        The name of the team.
    image_url : str
        The URL of the team's image.
    members : List[Member]
        A list of members in the team.
    """

    id: int
    name: str
    image_url: str
    members: List[Member]


@dataclass()
class Translator:
    """Represents a translator.

    Attributes
    ----------
    id : int
        The unique identifier for the translator.
    balance : Any
        The balance of the translator (e.g., points, currency).
    is_team : bool
        Indicates if the translator is part of a team.
    user : Optional[User]
        The user associated with the translator.
    team : Optional[Team]
        The team associated with the translator (if applicable).
    is_verified : bool
        Indicates if the translator is verified.
    """

    id: int
    balance: Any
    is_team: bool
    user: Optional[User]
    team: Optional[Team]
    is_verified: bool


@dataclass()
class Branch:
    """Represents a branch of a manga, including translator details.

    Attributes
    ----------
    id : int
        The unique identifier for the branch.
    translators : List[Translator]
        A list of translators for the branch.
    chapters_total : int
        The total number of chapters in the branch.
    likes_total : int
        The total number of likes for the branch.
    is_default : bool
        Indicates if the branch is the default one.
    subscription : Any
        The subscription details for the branch (if applicable).
    """

    id: int
    translators: List[Translator]
    chapters_total: int
    likes_total: int
    is_default: bool
    subscription: Any


@dataclass()
class Author:
    """Represents an author of a manga.

    Attributes
    ----------
    id : int
        The unique identifier for the author.
    name : str
        The name of the author.
    description : str
        A description of the author.
    image_url : str
        The URL of the author's image.
    """

    id: int
    name: str
    description: str
    image_url: str


@dataclass()
class Artist:
    """Represents an artist of a manga.

    Attributes
    ----------
    id : int
        The unique identifier for the artist.
    name : str
        The name of the artist.
    description : str
        A description of the artist.
    image_url : str
        The URL of the artist's image.
    """

    id: int
    name: str
    description: str
    image_url: str
