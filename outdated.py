months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()

    try:
        #NUMERIC FORMAT
        if "/" in date:
            month_str, day_str, year_str = date.split("/")
            month = int(month_str)
            day = int(day_str)
            year = int(year_str)

        #TEXT FORMAT
        elif "," in date:
            left_part, year_str = date.split(",")
            month_name, day_str = left_part.split()

            if month_name in months:
                month = months.index(month_name) + 1
            else:
                continue

            day = int(day_str)
            year = int(year_str)

        else:
            continue


        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year:04}-{month:02}-{day:02}")




    except ValueError:
        continue
