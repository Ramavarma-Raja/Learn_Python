class Task:
    def __init__(self, title, priority='low'):
        self.title = title
        self.priority = priority
        self.status = False

    def status_completed(self):
        self.status = True

def get_input(message, type=str):
    try:
        variable = input(message).strip()
        return type(variable) if type != str else variable
    except ValueError:
        display_message('Invalid Type')

def display_message(messages):
    if messages:
        for message in messages:
            print(message)
    
    del messages

def handle_input(tasks):
    title = get_input('Enter Task : ')

    for task in tasks:
        if title.lower() == task.title.lower():
            return 'Task Already Exist.'
        
    VALID_PRIORITY = {'high', 'medium', 'low'}
    
    priority = get_input('Enter Priority of Task (High/ Medium/ Low) : ')
    
    if priority.lower() in VALID_PRIORITY:
        tasks.append(Task(title, priority))
        return f'{title} Added.'
    else:
        return 'Invalid Priority.'

def handle_modification(tasks):
    handle_display(tasks, 'ongoing')

    index = get_input("Enter index of task to mark complete : ", int)
    index -= 1

    tasks[index].status_completed()
    return f'{tasks[index].title} marked complete.'

def handle_display(tasks, choice):
    i = 1
    messages = []

    if choice == 'ongoing':
        for task in tasks:
            if task.status is False:
                messages.append(f'{i}. {task.title}')
                i += 1
    
    if choice == 'completed':
        for task in tasks:
            if task.status is True:
                messages.append(f"{i}. {task.title}")
                i += 1
    
    return messages

def handle_delete(tasks):
    index = get_input("Enter index of task to be deleted : ", int)
    try:
        tasks.remove(index-1)
    except IndexError:
        display_message('Invalid Index')
    
    return f'{tasks[index-1].title} Removed.'

def main():
    tasks = []

    while True:
        print("Task Manager")
        print("------------")
        print("1. Add\n2. Mark as complete")
        print("3. View Ongoing Tasks\n4. View Completed Tasks")
        print("5. Delete Tasks\n6. Quit")

        try:
            choice = get_input('Enter Choice : ', int)
        except ValueError:
            print("Invalid Choice!")
            continue

        if choice == 6:
            print("Quiting")
            break

        if choice == 1:
            messages = handle_input(tasks)
        elif choice == 2:
            messages = handle_modification(tasks)
        elif choice == 3:
            messages = handle_display(tasks, 'ongoing')
        elif choice == 4:
            messages = handle_display(tasks, 'completed')
        elif choice == 5:
            messages = handle_delete(tasks)

        display_message(messages)

if __name__ == "__main__":
    main()