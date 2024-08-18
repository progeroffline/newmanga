from newmanga import NewMangaApi

api = NewMangaApi()

# Get first page from catalog
first_page = api.get_catalogue()

# Get first manga from catalog
manga_short_info = first_page.mangas[0]

# Get manga full info
if manga_short_info.slug:
    manga_full_info = api.get_manga(manga_short_info.slug)

    # Print result
    print(manga_full_info)
