def deposit(balance,amount):
    if amount > 0:
        balance += amount

    return balance

def withdraw(balance,amount):
    if amount <= balance:
        balance -= amount
        return balance

def check_balance(balance):
    print(f"Balance: {balance}")

hisob = 200

hisob = deposit(hisob,50)
check_balance(hisob)

hisob = withdraw(hisob,80)
check_balance(hisob)
