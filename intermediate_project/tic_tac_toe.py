import random

# Initialize the game state
board = ["-" for _ in range(9)]  # Create a list to represent the Tic-Tac-Toe board with 9 empty spots
currentPlayer = "X"  # Set the starting player to "X"
winner = None  # Variable to track the winner
gameRunning = True  # Variable to control the main game loop

# Function to print the Tic-Tac-Toe board
def printBoard(board):
    # Print the board in a 3x3 grid format
    print("\n")
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i+1] + " | " + board[i+2])
        if i < 6:
            print("---------")  # Print a separator between rows

# Function to take player input
def playerInput(board):
    # Loop until a valid input is received
    while True:
        try:
            inp = int(input(f"Player {currentPlayer}, select a spot (1-9): "))  # Ask the player to select a spot
            if inp < 1 or inp > 9:
                print("Invalid input. Please enter a number between 1 and 9.")  # Check if input is within valid range
            elif board[inp-1] != "-":
                print("Oops, that spot is already taken. Try again.")  # Check if the spot is already taken
            else:
                board[inp-1] = currentPlayer  # Place the player's mark on the board
                break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a number.")  # Handle non-integer inputs

# Function to check if there is a winner
def checkWin(board):
    # Define all possible winning combinations (rows, columns, diagonals)
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
                      (0, 4, 8), (2, 4, 6)]            # Diagonal
    # Check if any of the win conditions are met
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] != "-":
            return board[cond[0]]  # Return the winning player ("X" or "O")
    return None  # Return None if there is no winner yet

# Function to check if the game is a tie
def checkTie(board):
    return "-" not in board  # If there are no empty spots left, the game is a tie

# Function to switch players
def switchPlayer():
    # Switch the current player between "X" and "O"
    global currentPlayer
    currentPlayer = "O" if currentPlayer == "X" else "X"

# Function to handle the computer's move
def computerMove(board):
    # The computer randomly selects an empty spot to place "O"
    while currentPlayer == "O":
        position = random.randint(0, 8)  # Choose a random spot between 0 and 8
        if board[position] == "-":
            board[position] = "O"  # Place "O" on the board
            break  # Exit the loop after making a move

# Main game loop
while gameRunning:
    printBoard(board)  # Print the current board
    playerInput(board)  # Take input from the current player
    
    winner = checkWin(board)  # Check if there's a winner
    if winner:
        printBoard(board)
        print(f"The winner is {winner}!")  # Announce the winner
        break  # End the game
    
    if checkTie(board):
        printBoard(board)
        print("It's a tie!")  # Announce a tie if there are no empty spots
        break  # End the game
    
    switchPlayer()  # Switch to the other player
    computerMove(board)  # Let the computer make a move if it's "O"'s turn

    winner = checkWin(board)  # Check again if the computer won
    if winner:
        printBoard(board)
        print(f"The winner is {winner}!")  # Announce the winner
        break  # End the game
    
    if checkTie(board):
        printBoard(board)
        print("It's a tie!")  # Announce a tie if there are no empty spots
        break  # End the game
    
    switchPlayer()  # Switch back to the player "X"
