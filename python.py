def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6: #Length Check
        return False

    if not s[0].isalpha(): #First 2 characters to be letters
        return False
    if not s[1].isalpha():
        return False

    number_started = False

    for letter in s: #Punctuation & Space Check
        if not letter.isalnum():
            return False
        if letter .isdigit():
            number_started == False:
                if letter == "0":
                    return False
                number_started = True

        else:
            if number_started == True:
                return False


main()
