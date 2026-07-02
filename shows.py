SHOWS = [
    " avatar: the last airbender",
    "The Legend of korra",
    "The dragon prince",
    "Voltron: Legendary Defender",
    " spongebob squarepants",
    "the owl house",
    "Enchanted",
]


def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title()) #Strip removes whitespace from the beginning and end of the string, and title() capitalizes the first letter of each word.
                            



main()