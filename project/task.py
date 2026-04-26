def get_input():
    task = input("Enter Task : ").strip().lower()
    return task

def display_message(message):
    if message:
        print(message)

def add_item(tasks, task):
    if task in tasks:
        return False
    
    tasks.append(task)
    return True
    
def complete_task(tasks, completed_tasks, task):
    if tasks:
        if task in tasks:
            tasks.remove(task)
            completed_tasks.append(task)
            return f"'{task.title()}' Marked Completed."
        else:
            return f"'{task.title()}' Does Not Exist."
    else:
        return "No Tasks Logged."

def view_ongoing_tasks(tasks):
    if tasks:
        i = 1
        for task in tasks:
            print(f"{i}. {task.title()}")
            i += 1
    else:
        return "No Tasks Logged"

def view_completed_tasks(completed_tasks):
    if completed_tasks:
        i = 1
        for task in completed_tasks:
            print(f"{i}. {task.title()}")
            i += 1
    else:
        return "No Tasks Completed"

def delete_item(tasks, task):
    if tasks:
        if task not in tasks:
            return f"'{task.title()}' Not Found!"

        tasks.remove(task)
        
        return f"'{task.title()}' Deleted Successfully!"
    else:
        return "No Tasks Logged"

def main():
    tasks = []
    completed_tasks = []
    
    while True:
        print("\t\tDaily Task\n\t\t----------")      # title
        print("1. Add\n2. Mark as Completed\n3. View Ongoing Tasks")    # display functionalities
        print("4. View Completed Tasks\n5. Delete\n6. Exit")            # display functionalities

        try:    # try-except block added so that no type error occurs
            choice = int(input("Enter Choice : "))
        except ValueError:
            print("No such choices found")
            continue
        
        if choice == 6:    # to exit the program
            break

        if choice == 1:
            task = get_input()
            if add_item(tasks, task):
                display_message("Task Added.")
            else:
                display_message("Task Exists.")
        elif choice == 2:
            if tasks:
                view_ongoing_tasks(tasks)
                task = get_input()
                message = complete_task(tasks, completed_tasks, task)
            else:
                message = "No Tasks Found!"
            display_message(message)
        elif choice == 3:
            message = view_ongoing_tasks(tasks)
            display_message(message)
        elif choice == 4:
            message = view_completed_tasks(completed_tasks)
            display_message(message)
        elif choice == 5:
            view_ongoing_tasks(tasks)
            task = get_input()
            message = delete_item(tasks, task)
            display_message(message)

if __name__ == '__main__':
    main()