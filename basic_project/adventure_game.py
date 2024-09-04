def intro():
    # Introduction to the game
    print("Welcome to the Bomb Defusal Game!")
    print("You are a bomb squad specialist. Your mission is to defuse a bomb before time runs out.")
    print("The bomb has four wires: Red, Blue, Green, and Yellow.")
    print("Choose wisely, as cutting the wrong wire could be fatal!")
    
    # Call the first_choice function to start the decision-making process
    first_choice()

def first_choice():
    # Ask the player which wire they want to cut
    choice = input("Which wire do you want to cut? (Red/Blue/Green/Yellow): ").lower()
    
    # Check the player's choice and call the corresponding function
    if choice == "red":
        red_wire()
    elif choice == "blue":
        blue_wire()
    elif choice == "green":
        green_wire()
    elif choice == "yellow":
        yellow_wire()
    else:
        # If the input is invalid, prompt the player to try again
        print("Invalid choice. Try again.")
        first_choice()

def red_wire():
    # if the player cuts the Red wire
    print("You cut the Red wire.")
    print("The bomb exploded you got the wrong one the large damage was done to the place.")
    

def blue_wire():
    # if the player cuts the Blue wire
    print("You cut the Blue wire.")
    print("The bomb is defused. You win!")

def green_wire():
    # if the player cuts the Green wire
    print("You cut the Green wire.")
    print("The bomb was a decoy, and nothing happens. Everyone is safe.")
    
def yellow_wire():
    # if the player cuts the Yellow wire
    print("You cut the Yellow wire.")
    print("Boom! The bomb explodes. Game over.")

# Starting the game
intro()
