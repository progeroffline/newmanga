# Domain section
api_domain = "neo.newmanga.org"
api_v2_domain = "api.newmanga.org"
web_domain = "newmanga.org"
images_storage_domain = "img.newmanga.org"

# Endpoints section
catalogue = f"https://{api_domain}/catalogue"
manga = f"https://{web_domain}/p"
comments = "https://" + api_v2_domain + "/v2/projects/{slug}/comments"
similar = "https://" + api_v2_domain + "/v2/projects/{slug}/similar"
chapters = "https://" + api_v2_domain + "/v2/branches/{id}/chapters"
manga_api = f"https://{api_v2_domain}/v2/projects"

image_storage_url = f"https://{images_storage_domain}/ProjectCard/webp"

# Auth section
headers = {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
}
