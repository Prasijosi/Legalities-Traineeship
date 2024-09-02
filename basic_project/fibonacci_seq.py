# 7.Fibonacci Sequence Generator   

"""
The Fibonacci sequence is a set of numbers in which each is the sum of the two numbers before it.
It starts with zeros and ones. So, the sequence proceeds as follows:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
"""

"""
Recursion is a programming approach that involves calling a function on itself to solve a smaller version of the same problem.
A recursive function calls itself to calculate the previous two Fibonacci numbers until it reaches the base cases (0 and 1).
""" 

def fibonacci_sequence(i):
    # If the index is 0, return 0 (the first number in the Fibonacci sequence)
    if i == 0:
        return 0
    # If the index is 1, return 1 (the second number in the Fibonacci sequence)
    elif i == 1:
        return 1
    # For any index greater than 1, return the sum of the two preceding Fibonacci numbers
    else:
        return fibonacci_sequence(i-2) + fibonacci_sequence(i-1)

# Loop through the first 10 numbers (from 0 to 9)
for x in range(10):
    # Print each Fibonacci number followed by a space
    print(fibonacci_sequence(x), end=" ")
