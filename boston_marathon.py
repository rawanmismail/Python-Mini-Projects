def main():
    pace = get_pace(miles=26.2, minutes=180)
    print(f"You need to run each mile in {round(pace,2)} minutes.")
    #The {round(pace,2)} = Rounds the value of pace to 2 decimal places.

def get_pace(miles, minutes):
    if not minutes > 0:
