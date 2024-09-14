import os

def DirectoryTree(path, indent=""):
    """
    Recursively prints the directory tree structure for the given path.
    
    Args:
    path (str): The path to the directory.
    indent (str): The indentation to use for displaying the tree structure.
    """
    # List all items (files and directories) in the current directory
    items = os.listdir(path)
    
    # Iterate through each item in the directory
    for index, item in enumerate(items):
        # Create the full path of the current item (file or directory)
        full_path = os.path.join(path, item)
        
        # Check if the current item is the last one in the list
        if index == len(items) - 1:
            print(indent + "└── " + item)
            new_indent = indent + "    "
        else:
            print(indent + "├── " + item)
            new_indent = indent + "│   "
        
        # If the item is a directory, call the function recursively
        if os.path.isdir(full_path):
            """This is the recursive call. It allows the function to explore and print the
               contents of subdirectories. When a directory is found, the function calls itself
               with the new directory path (`full_path`) and the updated indentation (`new_indent`).
               This continues until all nested directories have been printed """
            DirectoryTree(full_path, new_indent)

def main():
    """
    Main function that prompts the user for a directory path
    and prints its directory tree structure.
    """
    directory_path = input("Enter the directory path to generate the tree: ")
    
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        print(directory_path)
        DirectoryTree(directory_path)
    else:
        print("Invalid directory path.")

main()
