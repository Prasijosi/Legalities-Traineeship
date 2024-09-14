# Word Frequency Counter
def create_file(filename): # create a new file to take input from user firstly
    texts = input("Write couple lines: ")

    # Create and write content to the file
    with open(filename, 'w') as file:
        file.write(texts )

def word_frequency(filename):
    # Empty dictionary to store word counts
    word_storage = {}

    # Open and read the text file
    with open(filename, 'r') as file:
        for line in file:
            
            # Split the line into words
            words = line.split()
            # Count each word
            for word in words:
                if word in word_storage:
                    word_storage[word] += 1
                else:
                    word_storage[word] = 1

    # Print each word with its frequency
    for word, count in word_storage.items():
        print(f"{word}:{count}")

# Defining the filename 
filename = 'wordfrequency.txt'
create_file(filename)
word_frequency(filename)
