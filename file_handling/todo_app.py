import os 
if not os.path.exists("tasks.txt"):
  with open("tasks.txt","x"):
    pass
def add_tasks():
  new_task =  input("Enter the task: ")
  with open("tasks.txt", "a") as file:
    file.write(f"{new_task}\n")
    print("Task Added.\n")

def view_tasks():
  with open("tasks.txt") as file:
    tasks = file.readlines()
    if not tasks:
      print("No tasks are present.")
    else:
      for i , task in enumerate(tasks,start=1):
        print(f"{i}. {task.strip()}")
def remove_task():
  removed_task = int(input("Enter the task number you want to delete: "))
  with open("tasks.txt") as file:
    tasks = file.readlines()
    if not tasks:
      print("No tasks are present")
    elif 0<removed_task<=len(tasks):
      print(f"Removed task: {tasks[removed_task-1]}")
      tasks.pop(removed_task-1)
      with open("tasks.txt","w") as f:
        f.writelines(tasks)
    else:
      print("Invalid input")

while True:
  print("Enter the function you wnat to perform:",
        "1.View tasks",
        "2.Add tasks",
        "3.Delete Task",
        "4.Exit",
        sep="\n")
  
  choice = input("").lower()
  if choice  == "exit" or choice == "4":
    print("Exited")
    break
  elif choice == "view tasks" or choice == "1":
    view_tasks()
  elif choice == "add tasks" or choice == "2":
    add_tasks()
  elif choice == "delete task" or choice == "3":
    remove_task()
  else:
    print("Invalid choice")
