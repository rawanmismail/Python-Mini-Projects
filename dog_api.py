#Project Info: Random Dog Picture & Breed Generator.

import requests

# 1. Define the API endpoint for a random dog picture
url = "https://dog.ceo/api/breeds/image/random"

# 2. Ask the API for data
response = requests.get(url)

