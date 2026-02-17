import requests
import os
from pathlib import Path

api_key = os.getenv("api_key")                            #enter your api key from pixabay api-Documentation page.
search_query = "WHAT_YOU_WANT_TO_SEARCH"                  #enter the search query to get results. 
per_page = 50                                             #enter the number of photos you want to download.
image_dir = "pixabay_images"                              #this is the directory where your photos is downloaded.

Path(image_dir).mkdir(exist_ok=True)

url = "https://pixabay.com/api/"
params = {
    "key": api_key,
    "q": search_query,
    "per_page": per_page,
    "image_type": os.getenv("image_type", "photo"),      #enter the image type you want (Accepted values: "all", "photo", "illustration", "vector").
    "order": "popular",                                  #enter the value to filter the results according to you want (Accepted values: "popular", "latest", "trending").
    "min_width": 1920,
    "min_height": 1080
}

response = requests.get(url, params=params)
data = response.json()

for i, image in enumerate(data.get("hits", []), 1):
    img_url = image["largeImageURL"]
    img_name = f"{search_query}_{i}.jpg"
    img_path = os.path.join(image_dir, img_name)
    
    img_response = requests.get(img_url)
    with open(img_path, "wb") as f:
        f.write(img_response.content)
    print(f"Downloaded: {img_name}")
