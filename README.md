
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

### Working example.
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


## Available types

<details>
<summary><b>MangaStatus</b></summary>

Enumeration for manga statuses:

- **`ON_GOING`**: Manga is ongoing.
- **`ABANDONED`**: Manga is abandoned.
- **`COMPLETED`**: Manga is completed.

</details>

<details>
<summary><b>MangaType</b></summary>

Enumeration for manga types:

- **`MANHYA`**: Korean vertical comics.
- **`MANHWA`**: Korean horizontal comics.
- **`MANGA`**: Japanese comics.
- **`RUSSIAN`**: Russian comics.
- **`COMICS`**: General comics.
- **`SINGLE`**: One-shot comics.
- **`OEL`**: Original English Language comics.

</details>

<details>
<summary><b>Manga</b></summary>

Represents detailed manga information:

- **`id`**: Unique identifier.
- **`slug`**: URL-friendly title.
- **`type`**: Type of manga (`MangaType`).
- **`rating`**: Average rating.
- **`rating_rank`**: Rating rank.
- **`likes`**: Number of likes.
- **`views`**: Number of views.
- **`status`**: Status of the manga (`MangaStatus`).
- **`adult`**: Adult content flag.
- **`tags`**: List of tags.
- **`genres`**: List of genres.
- **`count_chapters`**: Number of chapters.
- **`title_ru`**: Title in Russian.
- **`title_en`**: Title in English (optional).
- **`title_og`**: Original title (optional).
- **`image_small`**: Small cover image URL.
- **`image_large`**: Large cover image URL.
- **`url`**: Manga's page URL.
- **`description`**: Description of the manga.
- **`created_at`**: Creation timestamp.
- **`released_at`**: Release timestamp.
- **`released_year`**: Release year.
- **`is_active`**: Active status.

</details>

<details>
<summary><b>CatalogueResponse</b></summary>

Response from a catalogue query:

- **`mangas`**: List of `Manga` objects.
- **`page`**: Current page.
- **`found`**: Total mangas found.
- **`total`**: Total mangas available.

</details>

