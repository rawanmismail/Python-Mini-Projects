
Words = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to the Spelling Bee Game!")
    print("Your letters are: A  I  P  C  R  H  G")

    while len(Words) > 0:
        if guess == "EXIT":
            print("Thanks for playing!")
        elif guess in Words:
            print("Correct! You found a valid word!")
        else:
            print(f"Sorry, '{guess}' is not a valid word.")



main()