tasks = [
{"task":"Quran", "completed":False},
{"task":"Visit My Parents", "completed":True},
{"task":"Study", "completed":False},
{"task":"Exercise", "completed":True},
{"task":"Going to the Gym", "completed":False},
{"task":"Sleep", "completed":False},
]

def main():
    message = """
    1 - add tasks to a list
    2 - mark task as complete
    3 - view tasks
    4 - Quit
    """
    while True:
        print(message)
        choice = input("Enter your choice:")
        if choice == '1':
            add_task()
        elif choice == '2':
            mark_task_complete()
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            break
        else:
            print("Invalid choice, Please enter a number between 1 and 4")

def add_task():
    # get task from the user
    task = input("Enter Task: ")
    # define task status
    task_info = {"task": task, "completed":False}
    # add task to the list of tasks
    tasks.append(task_info)
    print("Task added to the list successfully")

def mark_task_complete():
    # get list of incomplete tasks
    incomplete_tasks = [task for task in tasks if task["completed"]==False]
    if not incomplete_tasks:
        print("no tasks to mark as complete")
        return
    # show them to the user
    for i, task in enumerate(incomplete_tasks):
        print(f'{i+1}-{task["task"]}')
        print('-'*30)
    
    # get the task from the user
    try:
        task_number = int(input("Choose the task number to complete: "))

        if task_number < 1 or task_number > len(incomplete_tasks):
            print("Invalid Task Number")
            return
        
        # mark the task as completed
        incomplete_tasks[task_number - 1]["completed"] = True

        #print a message to the user
        print ("Task marked as completed")
    except ValueError:
        print("Invalid Input")

def view_tasks():
    # if there are no tasks, print a message and return
    if not tasks:
        print("no tasks to view")
        return
    
    for i, task in enumerate(tasks):
        status = "✔" if task["completed"] else "✖"
        print(f'{i+1}. {task["task"]} {status}')

if __name__ == "__main__":
    main()
