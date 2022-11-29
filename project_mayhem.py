from project_mayhem import settle, transaction_input, view_user, user_name, view_all, read_balance, write_balance

running = True

read_balance()
user_name()
while running:
    action = input('Add transaction (i), view (v), log out (l): ')

    if action == "q":
        running = False
    
    elif action == "i":
        transaction_input()
        settle()
        write_balance()


    elif action == "v":
        settle()
        view_user()
    
    elif action == "l":
        user_name()
