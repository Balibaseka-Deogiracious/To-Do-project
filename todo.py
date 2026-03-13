
import os 
FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", encoding='utf-8') as file:
        tasks =file.read().splitlines()
    return tasks

def save_tasks(tasks):
    with open(FILE, "w", encoding='utf-8') as file:
        for task in tasks:
            file.write(task + "\n")

tasks =load_tasks()
while True:

    print("\n--- TO DO LIST---")                  
    print("1. Add Task")                  
    print("2. View Tasks")                  
    print("3. Complete Task")                  
    print("4. Delete Task")                  
    print("5. Exit")      

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter new task:")
        tasks.append("[] " + task)
        save_tasks(tasks)
        print("Task Added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
    elif choice == "3":
                 for i, task in enumerate(tasks):
                      print(f"{i+1}. {task}")
                 num = int(input("Enter task number completed: "))
                 if 0 < num <= len(tasks):
                      tasks[num-1] = tasks[num-1].replace("[]", "[✓]")
                      save_tasks(tasks)
                      print("Task marked as done!") 
    elif choice == "4":
         for i, task in enumerate(tasks):
              print(f"{i+1}. {task}")
         num = int(input("Enter task number to delete: "))
         if 0 < num <= len(tasks):
              tasks.pop(num-1)
              save_tasks(tasks)
              print("Task deleted!")
    elif choice == "5":
         break
    else:
         print("Invalid choice.")                                                      