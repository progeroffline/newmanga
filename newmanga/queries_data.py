catalogue = {
    "query": "",
    "sort": {
        "kind": "RATING",
        "dir": "DESC",
    },
    "filter": {
        "hidden_projects": [],
        "genres": {
            "excluded": [],
            "included": [],
        },
        "tags": {
            "excluded": [],
            "included": [],
        },
        "type": {
            "allowed": [],
        },
        "translation_status": {
            "allowed": [],
        },
        "released_year": {
            "min": None,
            "max": None,
        },
        "require_chapters": True,
        "original_status": {
            "allowed": [],
        },
        "adult": {
            "allowed": [
                "ADULT_13",
                "ADULT_16",
            ],
        },
    },
    "pagination": {
        "page": 2,
        "size": 32,
    },
}

comments = {"sort_by": "new"}
chapters = {
    "reverse": True,
    "page": 1,
    "size": 25,
}
popular = {
    "scale": "week",
    "page": 1,
    "size": 32,
}
updates = {
    "only_bookmarks": False,
    "page": 1,
    "size": 5,
}
