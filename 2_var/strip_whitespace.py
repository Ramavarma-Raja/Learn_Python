name = "ramavarma"
user_name = input("Enter name: ")

if (user_name.strip().lower()==name):
    print(f"Welcome, {name.title()}!")
else:
    print("Invalid Credentials!")