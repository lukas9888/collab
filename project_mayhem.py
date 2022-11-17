while True:
    
    amount_transactions = input() #input on amount of transactions

    if amount_transactions == 'q':
        break 

    else: 
        amount_transactions = int(amount_transactions)
        summed_transactions = []
        """
        The input for this lopp should be: payer reciver amount
        this for loop is tracing all the transaction and putting them in a list. 
        People who owe units will be given a positive value equal to their dept
        People who are owed units will be given a negative value equal to what they are owed
        """
        for x in range(int(amount_transactions)):  
            if amount_transactions >= 1 and amount_transactions <= 100000:
                tosplit = input().split()

                payer = tosplit[0]
                receiver = tosplit[1]
                amount = int(tosplit[2])
                
                summed_transactions.append([payer, - amount])
                summed_transactions.append([receiver, amount])

                
        def settle():
            """In this function will settle the dept between the payer and reciver and output the difference """
            transaction = {}
            for transaction in summed_transactions:
                if transaction[0] not in transaction:
                    transaction.setdefault(transaction[0], transaction[1])
                else:
                    total = transaction[1] + transaction[transaction[0]]
                    transaction[transaction[0]] = total
                
            print()
            for payer in transaction:
                for receiver in transaction:
                    if transaction[payer] > 0:
                        if transaction[receiver] < 0 and payer != receiver:
                            if -transaction[receiver] > transaction[payer]:
                                print(f"{payer} {receiver} {transaction[payer]}")
                                transaction[receiver] = transaction[receiver] + transaction[payer]
                                transaction[payer] = 0
                            else:    
                                print(f"{payer} {receiver} {-transaction[receiver]}")
                                transaction[payer] = transaction[payer] + transaction[receiver]
                                transaction[receiver] = 0
            print("settled")

        settle()
