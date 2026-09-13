import csv

with open('hogwarts.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)