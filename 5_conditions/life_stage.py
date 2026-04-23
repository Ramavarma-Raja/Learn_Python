ages = [1, 3, 10, 17, 45, 68]

for age in ages:
    if age >= 0 and age < 2:
        print("Baby!")
    elif age < 4:
        print("Toddler")
    elif age < 13:
        print("Kid")
    elif age < 20:
        print("Teenager")
    elif age < 65:
        print("Adult")
    else:
        print("Elder")