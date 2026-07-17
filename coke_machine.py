amount_due = 50

while amount_due > 0:
    print(f"Amount due: {amount_due} cents")
    coin = int(input("Insert coin (5, 10, 25): "))
    
    if coin in [5, 10, 25]:
        amount_due -= coin
