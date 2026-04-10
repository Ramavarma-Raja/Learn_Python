def add():    # function to add
    number1 = int(input("Enter number: "))
    number2 = int(input("Enter number: "))
    print(f"Sum = {number1 + number2}")
    main()

def subtract():  # function to subtract
    number1 = int(input("Enter number: "))
    number2 = int(input("Enter number: "))
    print(f"Difference = {number1 - number2}")
    main()

def multiply():     # function to multiply
    number1 = int(input("Enter number: "))
    number2 = int(input("Enter number: "))
    print(f"Product = {number1 * number2}")
    main()

def divide():       # function to divide
    number1 = int(input("Enter number: "))
    number2 = int(input("Enter number: "))
    print(f"Quotient = {number1 / number2}")
    main()

def main():    # main function for calculator body
    print("\t\tBasic Calculator\n\t\t---------------")      # title
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Quit")       # display functionalities
    choice = int(input("Choice: "))     # Enter choice from user
    if choice == 1:     
        add()       # function call to add
    elif choice == 2:
        subtract()      # function call to subtract
    elif choice == 3:
        multiply()      # function call to multiply
    elif choice == 4:
        divide()        # function call to divide
    elif choice == 5: 
        return      # exit program
    else:
        print("No such Option!")        # choice outside given range
    
    main()      # acts as infinite loop

if __name__ == "__main__":
    main()      # to initiate program