# 19.  Basic CRUD Application   

class ManageNotes:
    def __init__(self, filename):
        # Initialize the ManageNotes class with a dictionary to store notes and the filename to save/load notes from
        self.notes = {}
        self.filename = filename
        self.load_notes()

    def load_notes(self):
        # Load notes from the file into the dictionary
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    note = line.strip()  # Remove leading/trailing whitespace
                    self.notes[note] = note  # Store each note in the dictionary
        except FileNotFoundError:
            # If the file doesn't exist, start with an empty dictionary
            self.notes = {}

    def save_notes(self):
        # Save all notes from the dictionary to the file
        with open(self.filename, 'w') as file:
            for note in self.notes.values():
                file.write(f"{note}\n")  # Write each note on a new line

    def add_notes(self, note):
        # Add a new note to the dictionary and save it to the file
        self.notes[note] = note
        self.save_notes()
        print(f"New note '{note}' added successfully!")

    def view_notes(self):
        # Display all notes
        if not self.notes:
            print("No notes found.")
        else:
            for note in self.notes.values():
                print(f"Note: {note}")

    def search_notes(self, note):
        # Search for a specific note by its content
        if note in self.notes:
            print(f"Note: {note}")
        else:
            print(f"Note '{note}' not found.")

    def update_notes(self, old_note, new_note):
        # Update an existing note with new content
        if old_note in self.notes:
            del self.notes[old_note]  # Remove the old note
            self.notes[new_note] = new_note  # Add the new note
            self.save_notes()
            print(f"Note '{old_note}' updated to '{new_note}' successfully!")
        else:
            print(f"Note '{old_note}' not found.")

    def delete_notes(self, note):
        # Delete a note from the dictionary and save the changes
        if note in self.notes:
            del self.notes[note]
            self.save_notes()
            print(f"Note '{note}' deleted successfully!")
        else:
            print(f"Note '{note}' not found.")


def main():
    # Main function to run the note management application
    manage_notes = ManageNotes("notes.txt")  # Create an instance of ManageNotes with 'notes.txt' as the storage file

    while True:
        # Display menu options to the user
        print("\nNotes List\n")
        print("1. Add Note")
        print("2. View List Of Notes")
        print("3. Search Note")
        print("4. Update Note")
        print("5. Delete Note")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            note = input("Enter note: ")
            manage_notes.add_notes(note)  # Add a new note
            
        elif choice == '2':
            manage_notes.view_notes()  # View all notes
            
        elif choice == '3':
            note = input("Enter note to search: ")
            manage_notes.search_notes(note)  # Search for a specific note
            
        elif choice == '4':
            old_note = input("Enter the note to update: ")
            new_note = input("Enter the new note: ")
            manage_notes.update_notes(old_note, new_note)  # Update an existing note
            
        elif choice == '5':
            note = input("Enter the note to delete: ")
            manage_notes.delete_notes(note)  # Delete a note
            
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break  # Exit the program
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

main()
