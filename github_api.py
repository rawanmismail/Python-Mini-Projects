import requests

# We put your username directly in the API link!
username = "rawanmismail"
url = f"https://api.github.com/users/rawanmismail"

response = requests.get(url)

if response.status_code == 200: #MEANING: Did the server reply with 'Success'?
    user_data = response.json() #MEANING: Unpack the data into a Python dictionary
    print(f"User: {user_data.get('login')}") #MEANING: Look up the key 'login' (the username) and print it
    print(f"Public Repos: {user_data.get('public_repos')}") #MEANING: Get the 'public_repos' value from the dictionary and print it
else:
    print("Failed to retrieve user data.")

