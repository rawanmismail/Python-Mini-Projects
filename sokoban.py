
def main(): # Defines a function named main. The program’s logic is placed inside it.
    history = [] # Creates an empty list called history to store the actions the user enters

    while True:
        action = input("Enter an action (up, down, left, right) or 'undo' to undo the last action: ") # Prompts the user to enter an action and stores it in the variable action

        if action == "undo": # Checks if the user entered 'undo'
            if history: # Checks if there are any actions in the history list
                last_action = history.pop() # Removes the last action from the history list and stores it in last_action
                print(f"Undoing last action: {last_action}") # Prints a message indicating that the last action is being undone
            else:
                print("No actions to undo.") # Prints a message indicating that there are no actions to undo
        
