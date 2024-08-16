from enum import Enum


class MangaStatus(Enum):
    """Enumeration of possible statuses for a manga.

    Attributes
    ----------
    ON_GOING : str
        Indicates that the manga is currently ongoing.
    ABANDONED : str
        Indicates that the manga has been abandoned.
    COMPLETED : str
        Indicates that the manga is completed.
    SUSPENDED : str
        Indicates that the manga is currently suspended.
    ANNOUNCEMENT : str
        Indicates that the manga is in the announcement phase.
    """

    ON_GOING = "on_going"
    ABANDONED = "abandoned"
    COMPLETED = "completed"
    SUSPENDED = "suspended"
    ANNOUNCEMENT = "announcement"


class MangaType(Enum):
    """Enumeration of possible types for a manga.

    Attributes
    ----------
    MANHYA : str
        Indicates that the manga is a Manhya.
    MANHWA : str
        Indicates that the manga is a Manhwa.
    MANGA : str
        Indicates that the manga is a Manga.
    RUSSIAN : str
        Indicates that the manga is a Russian comic.
    COMICS : str
        Indicates that the manga is a general comic.
    SINGLE : str
        Indicates that the manga is a single volume.
    OEL : str
        Indicates that the manga is an Original English Language comic.
    """

    MANHYA = "manhya"
    MANHWA = "manhwa"
    MANGA = "manga"
    RUSSIAN = "russian"
    COMICS = "comics"
    SINGLE = "single"
    OEL = "oel"
