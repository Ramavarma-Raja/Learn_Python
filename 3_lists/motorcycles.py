motorcycles = []

def add_motorcycle():
    while True:
        motorcycle = input("Enter motorcycle (type exit to exit): ")
        if motorcycle.lower().strip() == 'exit':
            break
        motorcycles.append(motorcycle)
        print(f"{motorcycle} Added!")

def view_motorcycle():
    i = 1
    for motorcycle in motorcycles:
        print(f"{i}. {motorcycle.title()}")
        i += 1

def del_motorcycle():
    while True:
        view_motorcycle()
        motorcycle = input("Enter the option to be removed (type exit to exit): ")
        if motorcycle.strip().lower() == 'exit':
            break
        motorcycle = int(motorcycle)
        if motorcycle > 0 and motorcycle < len(motorcycles):
            del motorcycles[motorcycle-1]
        else:
            print("No such choices found!")

while True:
    print("1. Add to Motorcycle List")
    print("2. Disply Motorcycle List")
    print("3. Delete Motorcycle")
    print("4. Exit")
    
    choice = int(input("Enter Choice: "))
    if choice == 1:
        add_motorcycle()
    elif choice == 2:
        view_motorcycle()
        print('\n\n\n')
    elif choice == 3:
        del_motorcycle()
    elif choice == 4:
        break
    else:
        print("No such Choice found!")
        break