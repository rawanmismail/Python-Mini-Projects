from turtle import distance


distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU"
}

def main():
    spacecraft = input("Enter the name of the spacecraft: ")
    try:
        au = float(distances[spacecraft])
    except ValueError:
        print(f"Can't convert '{distances[spacecraft]}' to a float.")
        return
    except KeyError:
        print(f"'{spacecraft}' is not a valid spacecraft name in the dictionary.")
    
    m = convert(au)
    print(f"The distance of {spacecraft} from Earth is {m} meters away.")

def convert (au):
    return au * 149597870700


main()