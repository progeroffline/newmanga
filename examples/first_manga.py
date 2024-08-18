from newmanga import NewMangaApi

# Initialize the NewMangaApi client
api = NewMangaApi()

# Get the catalogue of manga without applying any search filters
catalogue = api.get_catalogue()

# Select the first manga from the catalogue
first_manga = catalogue.mangas[0]

# If the manga has a slug, fetch and print its detailed information
if first_manga.slug:
    print(api.get_manga(first_manga.slug))
