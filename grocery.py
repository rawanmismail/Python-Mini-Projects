# Step 1: Create an empty dictionary to keep track of items and their counts
grocery_list = {}

# Step 2: Keep asking the user for input using an infinite loop
while True:
    try:
        # Prompt the user for an item and immediately normalize it to uppercase
        item = input().strip().upper()

        # Ignore empty lines (if the user accidentally presses enter without typing anything)
        if not item:
            continue

        # Check if the item is already in our dictionary
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

    except EOFError:
        # Control-D (EOF) was pressed, break out of the input loop
        break

# Step 3: Print a blank line for clean output formatting
print()

# Step 4: Sort the dictionary keys alphabetically and print the count + item
for item in sorted(grocery_list): #to sort alphabetically
    print(f"{grocery_list[item]} {item}") #uses an f-string to combine the count and the item name (e.g. 3 APPLE)