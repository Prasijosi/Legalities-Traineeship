#String palindrome 
"""
A palindrome is a word, phrase, number, or other sequence of characters that reads the same 
forward and backward, ignoring spaces, punctuation, and capitalization.

"""
word = input("Enter a value: ")

# Reverse the input word using slicing [::-1] slice reverses the string.
reverse = word[::-1]

# To check if word is the same as its reversed version
if (word == reverse):
    print("It is Palindrome")
else:
    print("It is not Palindrome")