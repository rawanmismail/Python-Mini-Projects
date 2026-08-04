#Project Info: Random Dog Picture & Breed Generator.

import requests

# 1. Define the API endpoint for a random dog picture
url = "https://dog.ceo/api/breeds/image/random"

# 2. Ask the API for data
response = requests.get(url)

# 3. Check if the server responded with 200 (OK)
if response.status_code == 200:
    # 4. Convert the raw JSON into a Python dictionary
    data = response.json()
    
    # 5. Get the image URL from the dictionarys
    image_url = data.get("message")
    
    # 6. Extract the breed name from the image URL link
    # (e.g., "https://images.dog.ceo/breeds/husky/n02110185_1469.jpg" -> "husky")
    breed = image_url.split("/")[4]
    
    print("--- 🐶 Dog Found! ---")
    print(f"Breed: {breed.capitalize()}")
    print(f"Image Link: {image_url}")

