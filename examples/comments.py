from newmanga import NewMangaApi

# Initialize the NewMangaApi client
api = NewMangaApi()

# Get the catalogue of manga without applying any search filters
catalogue = api.get_catalogue()

# Select the first manga from the catalogue
first_manga = catalogue.mangas[0]

# Print the URL of the selected manga
print(first_manga.url)

# Fetch comments for the selected manga
for comment in first_manga.get_comments().comments:
    # Print the main comment text
    print(comment.text)

    # Print each reply to the main comment
    for sub_comment in comment.answers:
        print("---| " + sub_comment.text)

        # Print each reply to the sub-comment
        for sub_sub_comment in sub_comment.answers:
            print("------| " + sub_sub_comment.text)
