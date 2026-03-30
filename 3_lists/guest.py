guests = ['sanju', 'sangeeth', 'leo']

for guest in guests:
    print(f'Hey {guest.title()}, dont forget about the dinner tomorrow. Looking forward to see you at the dinner.\n\n')

name = input("Enter guests who cant come: ")
new_guest = input(f"Enter who replace {name}: ")

i = 0
for guest in guests:
    if name.lower().strip() == guest:
        del guests[i]
        guests.insert(i, new_guest)
    i += 1

print("Guest list: ")
for guest in guests:
    print(guest)