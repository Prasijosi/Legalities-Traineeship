import random
import os

def create_default_file(filename):
    """
    Creates a new file with some default quotes if the file doesn't exist.
    
    Args:
    filename (str): The name of the file to create.
    """
    default_quotes = [
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Get busy living or get busy dying. - Stephen King",
        "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy"
    ]
    
    with open(filename, 'w') as file:
        for quote in default_quotes:
            file.write(quote + '\n')
    print(f"'{filename}' created with random quotes.")

def load_quotes(filename):
   
    try:
        with open(filename, 'r') as file:
            quotes = [line.strip() for line in file.readlines() if line.strip()]
        return quotes
    except FileNotFoundError:
        print(f"The file '{filename}' was not found. '\n' Creating new one.")
        create_default_file(filename)
        return load_quotes(filename)

def display_random_quote(quotes):

    if quotes:
        random_quote = random.choice(quotes)
        print("\nRandom Quote: " + random_quote)
    else:
        print("No quotes available to display.")

def main():
    filename = 'randomquotes.txt'
    
    # Load quotes from the file (or create it if it doesn't exist)
    quotes = load_quotes(filename)
    
    display_random_quote(quotes)

main()
