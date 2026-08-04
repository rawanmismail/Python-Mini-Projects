import requests

# We put your username directly in the API link!
username = "rawanmismail"
url = f"https://api.github.com/users/rawanmismail"

response = requests.get(url)

