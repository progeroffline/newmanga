from enum import Enum


class MangaStatus(Enum):
    ON_GOING = "on_going"
    ABANDONED = "abandoned"
    COMPLETED = "completed"
    SUSPENDED = "suspended"
    ANNOUNCEMENT = "announcement"


class MangaType(Enum):
    MANHYA = "manhya"
    MANHWA = "manhwa"
    MANGA = "manga"
    RUSSIAN = "russian"
    COMICS = "comics"
    SINGLE = "single"
    OEL = "oel"
