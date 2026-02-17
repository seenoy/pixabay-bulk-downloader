import requests
import os
from pathlib import Path

api_key = os.getenv("api_key")
search_query = os.getenv("search_query")
per_page = os.getenv("per_page" , "50")
image_dir = "pixabay_images"                              #this is the directory where your photos is downloaded.
image_type = os.getenv("image_type", "photo")
order = os.getenv("order", "popular")

Path(image_dir).mkdir(exist_ok=True)

url = "https://pixabay.com/api/"
params = {
    "key": api_key,
    "q": search_query,
    "per_page": per_page,
    "image_type": image_type,
    "order": order,
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
