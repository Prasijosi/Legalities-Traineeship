word_list = ["apple", "banana", "cat", "dolphin", "elephant", "forest"]

def get_word():
    """
    Allows the user to select a word from the predefined list.
    """
    try:
        choice = int(input("Enter the number of your choice: ")) - 1
        if choice < 0 or choice >= len(word_list):
            print("Invalid choice! Please select a number between 1 and", len(word_list))
            return None
    except ValueError:
        print("Invalid input! Please enter a number.")
        return None

    word = word_list[choice].upper()
    return word

def play(word):
    """
    Manages the gameplay for Hangman.
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6

    print("Let's play the game!")
    print("Attempts left:", attempts)
    print(word_completion)
    print("\n")
    
    while not guessed and attempts > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print("Correct guess,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        
        print("Attempts left:", attempts)
        print(word_completion)
        print("\n")
    
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("You ran out of attempts. The word was " + word + ". Maybe next time!")

def main():
    """
    Main function to start the Hangman game.
    """
    while True:
        word = get_word()
        if word:
            play(word)
            break  

main()
