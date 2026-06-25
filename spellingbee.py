
Words = {"PAIR": 4, "HAIR": 4, "CHAIR": 5}

def main():
    print("Welcome to the Spelling Bee Game!")
    print("Your letters are: A  I  P  C  R  H  G")

    while len(Words) > 0:
        guess = input("Enter a word (or type 'exit' to quit): ").upper()
        if guess == "EXIT":
            print("Thanks for playing!")
        elif guess in Words:
            print("Correct! You found a valid word!")
        else:
            print(f"Sorry, '{guess}' is not a valid word.")

main()


main()