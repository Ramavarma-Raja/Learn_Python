def add_item(tasks):
    task = input("Enter Task : ")
    try:
        tasks.append(task)
    except ValueError:
        print("Error 404")
        return
    print("Item added Successfully")
    return tasks

def delete_item(tasks):
    if tasks:
        task = input("Enter task to be deleted")

        if task not in tasks:
            print("No such Task found!")
            return tasks

        while True:
            tasks.remove(task)
            if task not in tasks:
                break
        
        print("Task Deleted Successfully!")
        return tasks
    else:
        print("No Tasks Logged")
        return tasks

def view_item(tasks):
    if tasks:
        for task in tasks:
            print(f"> {task}")
    else:
        print("No Tasks Logged")

def main():
    tasks = []
    
    while True:
        print("\t\tDaily Task\n\t\t----------")      # title
        print("1. Add\n2. Delete\n3. View\n4. Exit")       # display functionalities

        try:    # try-except block added so that no type error occurs
            choice = int(input("Enter Choice : "))
        except ValueError:
            print("No such choices found")
            continue
        
        if choice == 4:    # to exit the program
            break

        if choice == 1:
            tasks = add_item(tasks)
        elif choice == 2:
            tasks = delete_item(tasks)
        elif choice == 3:
            view_item(tasks)

if __name__ == '__main__':
    main()