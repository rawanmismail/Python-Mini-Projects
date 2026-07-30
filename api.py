import json
from urllib.request import urlopen


def main():
    with urlopen("https://api.artic.edu/api/v1/artworks/search") as response:
        data = json.loads(response.read().decode("utf-8"))
        print(data)



main()