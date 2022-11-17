with open('balance.txt', 'a') as balance_text:
    for users in balance: 
        balance.write(f'{users}, {balance[users]}\n')
