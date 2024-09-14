class TodoListManager:
    def __init__(self, filename):
        # Initialized class with an empty list and a file to store the tasks
        self.tasks = []
        self.filename = filename
        # Load existing tasks from the file
        self.load_tasks()

    def load_tasks(self):
        # Try to open the file and load tasks from it
        try:
            with open(self.filename, 'r') as file:
                # Read each line from the file and strip any extra whitespace, then add to the tasks list
                self.tasks = [task.strip() for task in file.readlines()]
        except FileNotFoundError:
            # If the file doesn't exist, initialize an empty list of tasks
            self.tasks = []

    def save_tasks(self):
        # Open the file in write mode to save the tasks
        with open(self.filename, 'w') as file:
            # Write each task on a new line in the file
            for task in self.tasks:
                file.write(task + "\n")

    def add_task(self, task):
        # Add the new task to the list of tasks
        self.tasks.append(task)
        # Save the updated tasks list to the file
        self.save_tasks()
        # Print a confirmation message to the user
        print(f"Task '{task}' added successfully!")

    def view_tasks(self):
        # Check if there are any tasks in the list
        if not self.tasks:
            # If no tasks are found, inform the user
            print("No tasks found.")
        else:
            # If tasks are found, display each task with its number
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def delete_task(self, task_number):
        # Check if the task number is valid (within the range of tasks)
        if 0 < task_number <= len(self.tasks):
            # Remove the task at the specified index
            removed_task = self.tasks.pop(task_number - 1)
            # Save the updated tasks list to the file
            self.save_tasks()
            # Print a confirmation message to the user
            print(f"Task '{removed_task}' deleted successfully!")
        else:
            # If the task number is not valid, inform the user
            print(f"Task number {task_number} not found.")

def main():
    # Create an instance of the TodoListManager class, using "tasks.txt" as the file to store tasks
    todo_manager = TodoListManager("tasks.txt")

    while True:
        # Display a menu to the user
        print("\nTo-Do List\n")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        # Get the user's choice
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # If the user chooses to add a task, prompt for the task description
            task = input("Enter a new task: ")
            todo_manager.add_task(task)
            
        elif choice == '2':
            # If the user chooses to view tasks, display the list of tasks
            todo_manager.view_tasks()
            
        elif choice == '3':
            # If the user chooses to delete a task, prompt for the task number to delete
            task_number = int(input("Enter task number to delete: "))
            todo_manager.delete_task(task_number)
            
        elif choice == '4':
            # If the user chooses to exit, print a goodbye message and break the loop
            print("Exiting the program. Goodbye!")
            break
        else:
            # If the user enters an invalid choice, inform them and prompt again
            print("Invalid choice. Please enter a number between 1 and 4.")

# Call the main function to run the program
main()
