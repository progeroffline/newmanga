
# NewManga
This is not an official library written in python for getting manga from Newmanga website.


## Features
Unfortunately, it is now only possible to obtain data from the catalog, but soon there will be more options, stay tuned for updates.

- Search manga in catalogue

## Installing
```bash
pip install newmanga
```

## Usage

### Work with catalogue.
```python
from newmanga import NewMangaApi 

api = NewMangaApi()

# Get manga list without searching
api.get_catalogue()
""" Example answer
CatalogueResponse(
    mangas=[
        Manga(
            id=6724,
            slug='tears-on-a-withered-flower',
            type=<MangaType.MANHWA: 'manhwa'>,
            title_en='Tears On A Withered Flower',
            ...
            is_active=True
        )
    ],
    page=1,
    found=3170,
    total=4797
)
"""

# You can get a specific page
api.get_catalogue(page=10) # Default: 1

# You can search by keyword
api.get_catalogue(query="Sword") # Defalut: *

# You can change the amount of manga returned
api.get_catalogue(size=10) # Default: 32

# You can combine these arguments
api.get_catalogue(query="Sword", page=10, size=10)

# You can use the for loop to go through all the pages.
for page in api.get_catalogue.next_page(query="Sword", page=10, size=10):
    print(page)

```

### Work with manga.
```python
from newmanga import NewMangaApi 

api = NewMangaApi()

# Get first page from catalog
first_page = api.get_catalogue()

# Get first manga from catalog
manga_short_info = first_page.mangas[0]

# Get manga full info
manga_full_info = api.get_manga(manga_short_info.slug)
# Result
"""
Manga(
    id=6568,
    title_ru='Когда я стала сновидцем',
    title_en='When I became a Dream Walker',
    title_original='When I became a Dream Walker',
    image='https://img.newmanga.org/ProjectCard/webp/images/project_requests/6749/7a110b23-80d2-4314-977c-2a2ad19aaf18.webp',
    type=<MangaType.OEL: 'oel'>,
    rating=5.0,
    rating_count=None,
    hearts=11,
    views=57,
    bookmarks=18,
    status=<MangaStatus.ON_GOING: 'on_going'>,
    description=...,
    genres=[
        Genre(id=4, title_en='josai', title_ru='дзёсэй', title_original=None),
        Genre(id=30, title_en='fantastic', title_ru='фантастика', title_original=None),
        ...
        Genre(id=1, title_en='elements of humor', title_ru='элементы юмора', title_original=None)
    ],
    tags=[
        Tag(id=3, title_en='angels', title_ru='ангелы', title_original=None),
        Tag(id=10, title_en='gods', title_ru='боги', title_original=None),
        ...
        Tag(id=99, title_en='saving the world', title_ru='спасение мира', title_original=None)
    ],
    author=None,
    artist=None,
    release_date=datetime.datetime(2023, 10, 1, 0, 0),
    adult=13,
    tomes=[1],
    count_chapters=None,
    original_status=<MangaStatus.ON_GOING: 'on_going'>,
    slug='when-i-became-a-dream-walker',
    branches=[ ... ],
    original_url=None,
    english_url=None,
    other_url=None
)
"""
```
