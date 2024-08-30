# 3.Number Guessing Game   
secret_number = 5
i = 0
while i<5: # loop that runs for 5 times unless its correct hence giving users five possible chances to win
    num = int(input("Guess the Number: "))
    i += 1 #increment 
    
    if num == secret_number: #condition that if user guesses the secret number
        print("You have correctly guessed the number.")
        break #exits the loop when if statement is true
    
else: # if they dont correctly guess the number and run out of chances
    print("Better luck next time.")