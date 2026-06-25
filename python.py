Words = {"PAIR": 4, "HAIR": 4, "CHAIR": 5}

def main():
    print("Welcome to the Spelling Bee Game!")
    print("Your letters are: A  I  P  C  R  H  G")

    while len(Words) > 0:
        print(f"{len(Words)} left!")
        guess = input("Guess a word: ")
