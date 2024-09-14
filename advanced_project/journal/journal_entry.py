import datetime
import os

def write_entry():
    entry = input("Write your journal entry: ")
    with open(f"journal_{datetime.date.today().isoformat()}.txt", "w") as f:
        f.write(entry)
    print("Entry saved!")

def view_entries():
    entries = []
    for file in os.listdir():
        if file.startswith("journal_") and file.endswith(".txt"):
            with open(file, "r") as f:
                entries.append((file, f.read()))
    for file, entry in entries:
        print(f"Date: {file[7:-4]}")
        print(entry)
        print()

while True:
    print("Journal Application")
    print("1. Write a new entry")
    print("2. View all entries")
    print("3. Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        write_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        break
    else:
        print("Invalid option. Please try again.")