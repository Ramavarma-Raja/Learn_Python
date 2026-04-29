class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

def get_input(cars):
    brand = input("Enter brand : ")
    try:
        price = float(input("Enter Price : "))
    except ValueError:
        print("Price Format error!")
    
    cars.append(Car(brand, price))

def display_output(cars):
    for car in cars:
        print(f"Brand : {car.brand}")
        print(f"Price : {car.price}")

def main():
    cars = []

    get_input(cars)
    display_output(cars)

if __name__ == "__main__":
    main()