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
    m = convert(distance[spacecraft])
    print(f"The distance of {spacecraft} from Earth is {m} miles away.")

