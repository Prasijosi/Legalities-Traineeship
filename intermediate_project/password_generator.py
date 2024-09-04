# Password Generator 

import random

def generate_password(length):
    """Generates a random password of specified length."""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    return password

def main():
    """Prompts user for password length and generates password."""
    try:
        length = int(input("Enter desired password length (minimum 8 characters): "))
        if length < 8:
            raise ValueError("Password must be at least 8 characters long.")
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid number greater than or equal to 8.")
        return

    password = generate_password(length)
    print(f"Your password: {password}")

main()
