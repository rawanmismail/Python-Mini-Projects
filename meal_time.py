def main():
    time = input("What time is it? ")
    current = convert(time)

    if 7<= current <=8:
        print("Breakfast time")
    elif 12<= current <=13:
        print("Lunch time")
    elif 18<= current <=19:
        print("Dinner time")


def convert(time):
    hours, minutes = time.split(':')
    hours = int(hours)
    minutes = int(minutes)

    return hours + minutes / 60

if __name__ == "__main__":
    main()
