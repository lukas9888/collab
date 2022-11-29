user = ['']
def user_name():
    users = []
    with open('users.txt', 'r') as user_database:
        for usernames in user_database:
            usernames = usernames.rstrip()
            users.append(usernames)
    while True:
        username_input = input('Username: ') 
        if username_input in users:
            user[0] = username_input
            break
        else:
            create_new_user = input('Do you want to create a new user? (y/n)')
            if create_new_user == 'y':
                new_user_name()
                break
            else:
                continue
    return username_input



       
def new_user_name():
    existing_users = []
    with open('users.txt', 'r') as existing_users_text:
        for user in existing_users_text:
            user = user.rstrip()
            existing_users.append(user)

    while True: 
        new_name = input('New username: ')   
        if new_name not in existing_users:
            with open('users.txt', 'a') as user_text:
                user_text.write('\n' + new_name)
                break
        else:
            print('User allready exists')



transactions = []
def transaction_input():
    """The input should be: payer reciver amount
    this for loop is tracing all the transaction and putting them in a list. 
    People who owe units will be given a positive value equal to their debt
    People who are owed units will be given a negative value equal to what they are owed"""
    
    payer = user[0]
    amount_transactions = int(input('Amount of transactions: ')) #input on amount of transactions


    for x in range(amount_transactions):  
        if amount_transactions >= 1:
            tosplit = input().split()

            receiver = tosplit[0]
            amount = int(tosplit[1])
            
            transactions.append([payer, - amount])
            transactions.append([receiver, amount])


    

balance = {}
def settle():
    """This function will settle the debt between the payer and reciver and output the difference """
    with open('balance.txt', 'r') as balance_text: # This will read if there are any previous transactions made and put it in the dictonary 
        for users in balance_text:
            users = users.rstrip()
            user = users.split(',')
            if user[0] in balance.keys():
                balance[user[0]] += int(user[1])
            else:
                balance[user[0]] = int(user[1])

    for transaction in transactions:
        if transaction[0] not in balance:
            balance.setdefault(transaction[0], transaction[1])
        else:
            total = transaction[1] + balance[transaction[0]]
            balance[transaction[0]] = total
    with open('balance.txt', 'w') as balance_text: #this will save the transactions made into a dictonary 
        for users in balance: 
            balance_text.write(f'{users}, {balance[users]}\n')


def view():
    local_balance = balance
    for payer in local_balance:
        for receiver in local_balance:
            if local_balance[payer] > 0:
                if local_balance[receiver] < 0 and payer != receiver:
                    if -local_balance[receiver] > local_balance[payer]:
                        print(f"\n{payer} {receiver} {local_balance[payer]}")
                        local_balance[receiver] = local_balance[receiver] + local_balance[payer]
                        local_balance[payer] = 0
                    else:    
                        print(f"\n{payer} {receiver} {-local_balance[receiver]}")
                        local_balance[payer] = local_balance[payer] + local_balance[receiver]
                        local_balance[receiver] = 0
