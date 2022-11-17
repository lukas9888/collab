from project_mayhem import transaction_input, view

running = True

while running:
    action = input()
    
    if action == "q":
        running = False
    
    elif action == "input":
        transaction_input()


    elif action == "view":
        view()
