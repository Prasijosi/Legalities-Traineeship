# 19.  Basic CRUD Application   

class ManageNotes:
    def __init__(self, filename):
        self.notes = {}
        self.filename = filename
        self.load_notes()

    def load_notes(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    note = line.strip() 
                    self.notes[note] = note  
        except FileNotFoundError:
            # If the file doesn't exist, start with an empty dictionary
            self.notes = {}

    def save_notes(self):
        with open(self.filename, 'w') as file:
            for note in self.notes.values():
                file.write(f"{note}\n")  

    def add_notes(self, note):
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
        if note in self.notes:
            print(f"Note: {note}")
        else:
            print(f"Note '{note}' not found.")

    def update_notes(self, old_note, new_note):
        if old_note in self.notes:
            del self.notes[old_note]  
            self.notes[new_note] = new_note  
            self.save_notes()
            print(f"Note '{old_note}' updated to '{new_note}' successfully!")
        else:
            print(f"Note '{old_note}' not found.")

    def delete_notes(self, note):
        if note in self.notes:
            del self.notes[note]
            self.save_notes()
            print(f"Note '{note}' deleted successfully!")
        else:
            print(f"Note '{note}' not found.")


def main():
    manage_notes = ManageNotes("notes.txt")  # Create an instance of ManageNotes with 'notes.txt' as file

    while True:
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
            manage_notes.add_notes(note) 
            
        elif choice == '2':
            manage_notes.view_notes()  
            
        elif choice == '3':
            note = input("Enter note to search: ")
            manage_notes.search_notes(note)  
            
        elif choice == '4':
            old_note = input("Enter the note to update: ")
            new_note = input("Enter the new note: ")
            manage_notes.update_notes(old_note, new_note)  
            
        elif choice == '5':
            note = input("Enter the note to delete: ")
            manage_notes.delete_notes(note) 
            
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break 
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

main()
