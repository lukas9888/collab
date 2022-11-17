def transaction_input():
    """The input should be: payer reciver amount
    this for loop is tracing all the transaction and putting them in a list. 
    People who owe units will be given a positive value equal to their debt
    People who are owed units will be given a negative value equal to what they are owed"""
    transactions = []
    amount_transactions = int(input()) #input on amount of transactions

    for x in range(amount_transactions):  
        if amount_transactions >= 1:
            tosplit = input().split()

            payer = tosplit[0]
            receiver = tosplit[1]
            amount = int(tosplit[2])
            
            transactions.append([payer, - amount])
            transactions.append([receiver, amount])
    return transactions

balance = {}
def settle():
    """This function will settle the debt between the payer and reciver and output the difference """
    for transaction in transactions:
        if transaction[0] not in balance:
            balance.setdefault(transaction[0], transaction[1])
        else:
            total = transaction[1] + balance[transaction[0]]
            balance[transaction[0]] = total

def view():
    local_balance = balance
    for payer in local_balance:
        for receiver in local_balance:
            if local_balance[payer] > 0:
                if local_balance[receiver] < 0 and payer != receiver:
                    if -local_balance[receiver] > local_balance[payer]:
                        print(f"{payer} {receiver} {local_balance[payer]}")
                        local_balance[receiver] = local_balance[receiver] + local_balance[payer]
                        local_balance[payer] = 0
                    else:    
                        print(f"{payer} {receiver} {-local_balance[receiver]}")
                        local_balance[payer] = local_balance[payer] + local_balance[receiver]
                        local_balance[receiver] = 0
