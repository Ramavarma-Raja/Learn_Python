alien_color = ['green', 'yellow', 'red']

for color in alien_color:
    if color.lower() == 'green':
        print("+5 Points!")
    elif color.lower() == 'yellow':
        print("+10 Points!")
    elif color.lower() == 'red':
        print("+15 Points!")
    else:
        print("Easter Egg!")