from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass()
class Genre:
    id: int | None = None
    title_en: str | None = None
    title_ru: str | None = None
    title_original: str | None = None


@dataclass()
class Tag:
    id: int | None = None
    title_en: str | None = None
    title_ru: str | None = None
    title_original: str | None = None


@dataclass()
class User:
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
    id: int
    user: User | None
    statuses: list[str]


@dataclass()
class Team:
    id: int
    name: str
    image_url: str
    members: list[Member]


@dataclass()
class Translator:
    id: int
    balance: Any
    is_team: bool
    user: User | None
    team: Team | None
    is_verified: bool


@dataclass()
class Branch:
    id: int
    translators: list[Translator]
    chapters_total: int
    likes_total: int
    is_default: bool
    subscription: Any


@dataclass()
class Author:
    id: int
    name: str
    description: str
    image_url: str


@dataclass()
class Artist:
    id: int
    name: str
    description: str
    image_url: str
