
#Harvard CS50 Python Course Follow Through



def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for name in names:
        print(write_letter(name, "Princess Peach"))




def write_letter(reciever, sender):
    return f"""
    -----------------------------------------------------
    Dear {reciever},

    You are cordially invited to a ball at Peache's Castle
    this evening at 7:00 PM. Please come dressed in 
    your finest attire.

    Sincerely,
    {sender}
    -----------------------------------------------------
    """

main()