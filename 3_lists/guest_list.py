guests = []

def add_guest():
    guest = input("Enter guest name: ")
    guest = guest.strip().lower()
    guests.append(guest)
    choice = input("Want to continue? (y/n): ")
    choice = choice.lower().strip()
    if choice == 'y' or choice == 'yes':
        add_guest()
    elif choice == 'n' or choice == 'no':
        print("Guest List updated!")
        return
    else:
        print("No such option!")
        add_guest()

def view_guest():
    if len(guests) == 0:
        print("List Empty!")
        return
    i = 1
    for guest in guests:
        print(f"{i}. {guest.title()}")
        i += 1

def replace_guest():
    i = 0
    view_guest()
    guest_old = input("Enter guest to be replaced: ")
    guest_new = input(f"Enter guest to replace {guest_old}: ")
    for guest in guests:
        if guest_old.lower().strip() == guest:
            del guests[i]
            guests.insert(i, guest_new)
        i += 1
    print("List updated!")
    choice = input("Want to continue? (y/n) ")
    choice = choice.lower().strip()
    if choice == 'y' or choice == 'yes':
        replace_guest()
    elif choice == 'n' or choice == 'no':
        print("Returning to main menu!")
        return
    else:
        print("No such options")
        replace_guest()

def del_guest():
    view_guest()
    guest_old = input("Enter name of guest to be removed: ")
    guests.remove(guest_old)
    choice = input("Want to continue? (y/n): ")
    choice = choice.strip().lower()
    if  choice == 'y' or choice == 'yes':
        del_guest()
    elif choice == 'n' or choice == 'no':
        print("Returning to main menu!")
        return
    else:
        print("No such option found!")
        del_guest()

while True:
    print(f"MENU Total Count: {len(guests)}\n----\n1. Add Guests\n2. View Guests\n3. Replace Guests\n4. Delete Guest\n5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        add_guest()
    elif choice == 2:
        view_guest()
    elif choice == 3:
        replace_guest()
    elif choice == 4:
        del_guest()
    elif choice == 5:
        break
    else:
        print("No such options found!")