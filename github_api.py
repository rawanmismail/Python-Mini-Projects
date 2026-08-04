import requests

# We put your username directly in the API link!
username = "rawanmismail"
url = f"https://api.github.com/users/rawanmismail"

response = requests.get(url)

if response.status_code == 200: #MEANING: Did the server reply with 'Success'?
    user_data = response.json() #MEANING: Unpack the data into a Python dictionary
