from plyer import notification
import time
import os

def load_tasks(filename):
    tasks = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                task_details = line.strip().split('|')
                if len(task_details) == 3:
                    task, timestamp, reminder = task_details
                    tasks.append((task, float(timestamp), reminder))
    return tasks

def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        for task, timestamp, reminder in tasks:
            file.write(f"{task}|{timestamp}|{reminder}\n")

def add_task(tasks):
    task = input("Enter the task description: ")
    reminder_time = float(input("Enter reminder time in seconds from now: "))
    reminder = input("Enter reminder message: ")
    timestamp = time.time() + reminder_time
    tasks.append((task, timestamp, reminder))
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nScheduled Tasks:")
    for i, (task, timestamp, reminder) in enumerate(tasks):
        due_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
        print(f"{i + 1}. Task: {task}, Due Time: {due_time}, Reminder: {reminder}")

def check_reminders(tasks):
    current_time = time.time()
    for task, timestamp, reminder in tasks:
        if current_time >= timestamp:
            # Use system notification to alert the user
            notification.notify(
                title='Task Reminder',
                message=f"Reminder: {reminder} - Task: {task}",
                timeout=10  # Notification duration in seconds
            )
            tasks.remove((task, timestamp, reminder))  

def main():
    filename = 'tasks.txt'
    tasks = load_tasks(filename)
    
    check_reminders(tasks)
    
    while True:
        print("\nTask Scheduler")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Check Reminders")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            check_reminders(tasks)
        elif choice == '4':
            save_tasks(tasks, filename)
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

main()
