import random

def spr(player1, computer):
    """
    Determines the winner of a Rock-Paper-Scissors game.
    - If the choices are the same, it's a tie.
    - Determines the winner based on the rules of Rock-Paper-Scissors.
    """
    if player1 == computer:
        return "It's a tie!"

    elif (player1 == "Rock" and computer == "Scissors") or \
         (player1 == "Paper" and computer == "Rock") or \
         (player1 == "Scissors" and computer == "Paper"):
        return "Player wins!"

    else:
        return "Computer wins!"

picks = ["rock", "paper", "scissors"]

while True:
    try:
        player1 = input("Enter your choice Rock, Paper or Scissors: ").lower()

        if player1 in picks: # checking if picks is valid
            break
        else:
            print("Choose Rock, Paper or Scissors.\n")

    except ValueError: # Handle errors like if you write other things instead of available picks
        print("Invalid Input.")

# Generate computer's picks randomly from random that we imported
computer_pick = random.choice(picks)
print(f"Computer picked: {computer_pick}")

# Determine winner using spr function and print the WINNER
winner = spr(player1.capitalize(), computer_pick.capitalize())
print(winner)
