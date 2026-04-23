users = ['ram', 'ghost', 'goggins', 'user1', 'guest_user', 'admin']

loged_in = ['ram', 'admin', 'ram', 'user1', 'ghost_root']

if users:
    for user in loged_in:
        if user in users:
            if user == 'admin':
                print(f"Hello {user}! Would you like to see the status report?")
            else:
                print(f"Hello, {user}!")
        else:
            print(f"{user} tried to login")

else:
    print("Installation not complete!")