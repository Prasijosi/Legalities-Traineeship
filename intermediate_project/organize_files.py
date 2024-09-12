import os
""" The os module in Python provides a way of interacting with the operating system.
It offers a range of functions to work with file systems, directories, paths, processes,
and more, allowing developers to perform operating system-level tasks programmatically."""

def OrganizeFiles(directory):
    """
    Organizes files in the specified directory based on their file types (extensions).
    
    Args:
    directory (str): The path of the directory to organize.
    """
    # Check if the provided directory exists
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return
    
    # Create a dictionary to categorize files based on their extensions
    file_types = {}

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Get the file path
        file_path = os.path.join(directory, filename)

        # Ignore directories, only focus on files
        if os.path.isfile(file_path):
            # Get the file extension (without the dot)
            file_extension = filename.split('.')[-1]

            # Add the file to its respective file type category
            if file_extension not in file_types:
                file_types[file_extension] = []
            file_types[file_extension].append(filename)

    # Create directories for each file type and move files into them
    for file_extension, files in file_types.items():
        # Create a directory for the file extension if it doesn't exist
        ext_dir = os.path.join(directory, file_extension.upper())
        if not os.path.exists(ext_dir):
            os.mkdir(ext_dir)
        
        # Move each file into its respective directory
        for file in files:
            old_path = os.path.join(directory, file)
            new_path = os.path.join(ext_dir, file)
            os.rename(old_path, new_path)  # Move the file

    print("Files have been organized based on their types!")

def main():
    """
    Main function to execute the file organizer.
    """
    directory = input("Enter the directory path to organize: ")
    OrganizeFiles(directory)

main()
