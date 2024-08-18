from newmanga import NewMangaApi

api = NewMangaApi()

# Get manga list without searching
api.get_catalogue()

# You can get a specific page
api.get_catalogue(page=10)  # Default: 1

# You can search by keyword
api.get_catalogue(query="Sword")  # Defalut: *

# You can change the amount of manga returned
api.get_catalogue(size=10)  # Default: 32

# You can combine these arguments
api.get_catalogue(query="Sword", page=10, size=10)

# You can use the for loop to go through all the pages.
for page in api.get_catalogue.next_page(query="Sword", page=10, size=10):
    print(page)
