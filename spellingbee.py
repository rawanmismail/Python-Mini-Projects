
Words = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to the Spelling Bee Game!")
    print("Your letters are: A  I  P  C  R  H  G")

    while len(Words) > 0:
        guess = input("Guess the word:" + " ").strip().upper()
        print("Your guess is:", repr(guess))

        if guess == "GRAPHIC":
            points = Words[guess]
            print(f"Congratulations! You have won! You scored {points} points!")

        elif guess in Words:


        else:
            print(f"Sorry, '{guess}' is not a valid word.")



main()