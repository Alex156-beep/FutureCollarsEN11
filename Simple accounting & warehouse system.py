balance = 0
warehouse = {}
operations = []

commands = [
    "balance", "sale", "purchase",
    "account", "list", "warehouse",
    "review", "end"
]

def show_commands():
    print("\nCommands:")
    for c in commands:
        print(" -", c)

show_commands()

while True:
    cmd = input("\nEnter command: ").lower()

    # ---------------- BALANCE ----------------
    if cmd == "balance":
        try:
            amount = int(input("Amount (+/-): "))
            balance += amount
            operations.append(f"balance {amount}")
        except:
            print("Invalid number.")
        show_commands()

    # ---------------- SALE ----------------
    elif cmd == "sale":
        product = input("Product name: ")
        try:
            price = int(input("Price: "))
            qty = int(input("Quantity: "))
        except:
            print("Invalid number.")
            show_commands()
            continue

        if product not in warehouse or warehouse[product]["quantity"] < qty:
            print("Not enough stock.")
        else:
            warehouse[product]["quantity"] -= qty
            balance += price * qty
            operations.append(f"sale {product} {price} {qty}")

        show_commands()

    # ---------------- PURCHASE ----------------
    elif cmd == "purchase":
        product = input("Product name: ")
        try:
            price = int(input("Price: "))
            qty = int(input("Quantity: "))
        except:
            print("Invalid number.")
            show_commands()
            continue

        cost = price * qty

        if balance - cost < 0:
            print("Not enough funds.")
        else:
            balance -= cost

            if product not in warehouse:
                warehouse[product] = {"price": price, "quantity": qty}
            else:
                warehouse[product]["quantity"] += qty
                warehouse[product]["price"] = price

            operations.append(f"purchase {product} {price} {qty}")

        show_commands()

    # ---------------- ACCOUNT ----------------
    elif cmd == "account":
        print("Balance:", balance)
        show_commands()

    # ---------------- LIST ----------------
    elif cmd == "list":
        print("\nWarehouse:")
        for p, data in warehouse.items():
            print(p, "→ price:", data["price"], "quantity:", data["quantity"])
        show_commands()

    # ---------------- WAREHOUSE ----------------
    elif cmd == "warehouse":
        product = input("Product name: ")
        if product in warehouse:
            print(product, "→", warehouse[product])
        else:
            print("Not found.")
        show_commands()

    # ---------------- REVIEW ----------------
    elif cmd == "review":
        start = input("From index: ")
        end = input("To index: ")

        if start == "":
            start = 0
        if end == "":
            end = len(operations)

        try:
            start = int(start)
            end = int(end)
        except:
            print("Invalid index.")
            show_commands()
            continue

        if start < 0 or end > len(operations):
            print("Index out of range.")
        else:
            for op in operations[start:end]:
                print(op)

        show_commands()

    # ---------------- END ----------------
    elif cmd == "end":
        print("Goodbye!")
        break

    # ---------------- INVALID ----------------
    else:
        print("Unknown command.")
        show_commands()

