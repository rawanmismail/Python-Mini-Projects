""" The program tests the following:
1. Getting input from the user
2. Converting a string to camel case
3. Checking if a letter is uppercase 

The whole concept in simple terms:
The user will enter variablename in camelCase
My program will then convert it to snake_case
"""


camel = input("camelCase:  ") #Get the input from the user
for letter in camel: #Loop through each letter in the input string
    if letter.isupper(): #Check if the letter is uppercase
        print("_" + letter.lower(), end = "") #If it is, print an underscore and the lowercase version of the letter
    else:
        print(letter, end = "") #If it isn't, print the letter as is