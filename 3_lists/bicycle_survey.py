bicycles = ['trek', 'firefox', 'hercules', 'hero', 'cannondale', 'redline', 'specialized']
i = 1
message = "My first cycle was a "

for bicycle in bicycles:
    print(f'{i}. {bicycle}')
    i += 1

choice = int(input("Enter your first cycle (as number): "))

if choice > 0 and choice < 8:
    print(f"{message} {bicycles[choice-1].title()}")
else:
    print("No such options.")