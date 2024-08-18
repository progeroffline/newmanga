from newmanga import NewMangaApi

# Initialize the NewMangaApi client
api = NewMangaApi()

# Get the catalogue of manga without applying any search filters
catalogue = api.get_catalogue()

# Select the first manga from the catalogue
first_manga = catalogue.mangas[0]

# Print the URL of the selected manga
print(first_manga.url)

# Fetch similar for the selected manga
for manga in first_manga.get_similar().mangas:
    print(manga)