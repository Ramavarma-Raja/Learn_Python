class Task:
    def __init__(self, title, priority='low'):
        self.title = title
        self.priority = priority
        self.status = False
    
    def status_update(self):
        self.status = not(self.status)

def ui_display():
    print("Task Manager")
    print("------------")
    print("1. Add Tasks\n2. Complete Tasks")
    print("3. View Tasks\n4. View Completed Tasks")
    print("5. Delete Tasks\n6. Quit")
    try:
        return int(input("Enter Choice : "))
    except ValueError:
        print("Invalid Choice.")
        return None

def handle_quit():
    choice = input("Are you sure you want to quit? (y/n) : ")

    if choice.lower() == 'y':
        print("Quiting.")
        return True
    elif choice.lower() == 'n':
        return False
    else:
        print("Invalid Choice.")
        return False

def main():
    while True:
        choice = ui_display()

        if isinstance(choice, int):
            pass
        else:
            continue

        if choice == 6:
            flag = handle_quit()

            if flag is True:
                break

if __name__ == "__main__":
    main()