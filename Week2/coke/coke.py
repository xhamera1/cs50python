due = 50
while due > 0:
    print(f"Amount Due: {due}")
    inserted = int(input("Insert Coin: "))
    if inserted in [5, 10, 25]:
        due -= inserted
    else:
        continue
    if due <= 0:
        print(f"Change Owed: {abs(due)}")
        break
