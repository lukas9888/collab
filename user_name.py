username_input = ''
def user_name():
    users = []
    with open('users.txt', 'r') as user_database:
        for usernames in user_database:
            usernames = usernames.rstrip()
            users.append(usernames)
    while True:
        username_input = input('Username: ') 
        if username_input in users:
            username_input = username_input
            break
