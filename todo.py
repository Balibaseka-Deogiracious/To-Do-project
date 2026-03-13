# import sys


# def load_tasks():
#     try:
#         with open("tasks.txt", "r") as file:
#             tasks = file.read().splitlines()
#         return tasks
#     except FileNotFoundError:
#         return []


# def save_tasks(tasks):
#     with open("tasks.txt", "w") as file:
#         for task in tasks:
#             file.write(task + "\n")


# def main():
#     tasks = load_tasks()

#     while True:
#         print("\n---  TO DO LIST ---")
#         print("1. Add Task")
#         print("2. View Tasks")
#         print("3. Delete Task")
#         print("4. Exit")

#         choice = input("Choose an option: ")

#         if choice == "1":
#             task = input("Enter task: ")
#             tasks.append(task)
#             save_tasks(tasks)
#             print("Task added!")

#         elif choice == "2":
#             if not tasks:
#                 print("No tasks found.")
#             else:
#                 print("\nTasks:")
#                 for i, task in enumerate(tasks, start=1):
#                     print(f"{i}. {task}")

#         elif choice == "3":
#             if not tasks:
#                 print("No tasks to delete.")
#                 continue

#             for i, task in enumerate(tasks, start=1):
#                 print(f"{i}. {task}")

#             num_str = input("Enter task number to delete: ")
#             if not num_str.isdigit():
#                 print("Invalid number")
#                 continue

#             num = int(num_str)
#             if 1 <= num <= len(tasks):
#                 tasks.pop(num - 1)
#                 save_tasks(tasks)
#                 print("Task removed!")
#             else:
#                 print("Invalid number")

#         elif choice == "4":
#             print("Goodbye!")
#             break

#         else:
#             print("Invalid option")


# if __name__ == "__main__":
#     try:
#         main()
#     except KeyboardInterrupt:
#         print("\nGoodbye!")
#         sys.exit(0)


import os 
FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as file:
        tasks =file.read().splitlines()
    return tasks

def save_tasks(tasks):
    with open(FILE, "r")      