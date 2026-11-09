balance = 5000

def buy_some(item, value):
    global balance
    balance -= value
    print(f'Balance after {item} buing', balance)

print("Balance befor buing", balance)
buy_some("Mouse", 1550)
