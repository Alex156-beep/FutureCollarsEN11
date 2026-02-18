import os
import ast

# ============================================================
# DATA CLASSES
# ============================================================

class WarehouseItem:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {"price": self.price, "quantity": self.quantity}

    @staticmethod
    def from_dict(data):
        return WarehouseItem(data["price"], data["quantity"])


# ============================================================
# SYSTEM CLASS
# ============================================================

class AccountingSystem:
    def __init__(self):
        self.balance = 0
        self.warehouse = {} # {product: WarehouseItem}
        self.history = [] # list of operations

        print(">>> In __init__, loading data...")
        self.load_data()

    # ------------------------------------------------------
    # FILE LOADING
    # ------------------------------------------------------
    def load(self, filename, default):
        """Safe file loader with literal_eval()"""
        if not os.path.exists(filename):
            return default

        try:
            with open(filename, "r") as f:
                content = f.read().strip()
                return ast.literal_eval(content)
        except Exception:
            print(f"Warning: Could not read '{filename}', using defaults.")
            return default

    def load_data(self):
        self.balance = self.load("balance.txt", 0)
        raw_warehouse = self.load("warehouse.txt", {})
        self.history = self.load("history.txt", [])

        # Recreate warehouse objects
        for name, data in raw_warehouse.items():
            self.warehouse[name] = WarehouseItem.from_dict(data)

    # ------------------------------------------------------
    # SAVING DATA
    # ------------------------------------------------------
    def save(self, filename, data):
        with open(filename, "w") as f:
            f.write(str(data))

    def save_data(self):
        self.save("balance.txt", self.balance)
        self.save("history.txt", self.history)
        # Convert warehouse objects to dicts
        warehouse_dict = {name: item.to_dict() for name, item in self.warehouse.items()}
        self.save("warehouse.txt", warehouse_dict)

    # ------------------------------------------------------
    # COMMAND HANDLERS
    # ------------------------------------------------------
    def do_balance(self):
        try:
            amount = int(input("Amount (+/-): "))
            self.balance += amount
            self.history.append(("balance", amount))
        except ValueError:
            print("Invalid number.")

    def do_purchase(self):
        name = input("Product: ")
        try:
            price = int(input("Price: "))
            qty = int(input("Quantity: "))
        except ValueError:
            print("Invalid input.")
            return

        cost = price * qty
        if self.balance < cost:
            print("Not enough money.")
            return

        self.balance -= cost

        if name not in self.warehouse:
            self.warehouse[name] = WarehouseItem(price, qty)
        else:
            item = self.warehouse[name]
            item.quantity += qty
            item.price = price # update price

        self.history.append(("purchase", name, price, qty))

    def do_sale(self):
        name = input("Product: ")
        try:
            price = int(input("Price: "))
            qty = int(input("Quantity: "))
        except ValueError:
            print("Invalid input.")
            return

        if name not in self.warehouse or self.warehouse[name].quantity < qty:
            print("Not enough stock.")
            return

        item = self.warehouse[name]
        item.quantity -= qty
        self.balance += price * qty

        self.history.append(("sale", name, price, qty))

    def list_warehouse(self):
        for name, item in self.warehouse.items():
            print(f"{name}: price={item.price}, qty={item.quantity}")

    def show_product(self):
        name = input("Product: ")
        if name in self.warehouse:
            item = self.warehouse[name]
            print(f"{name}: price={item.price}, qty={item.quantity}")
        else:
            print("Product not found.")

    def show_account(self):
        print("Balance:", self.balance)

    def do_review(self):
        start = input("From index (empty = 0): ")
        end = input("To index (empty = end): ")

        start = int(start) if start else 0
        end = int(end) if end else len(self.history)

        if start < 0 or end > len(self.history):
            print("Index out of range.")
            return

        for entry in self.history[start:end]:
            print(entry)

    # ------------------------------------------------------
    # MAIN MENU
    # ------------------------------------------------------
    def run(self):
        print(">>> Entered run()")
        print("Commands: balance | purchase | sale | account | list | warehouse | review | end")

        while True:
            cmd = input("\nCommand: ").lower()

            if cmd == "balance":
                self.do_balance()

            elif cmd == "purchase":
                self.do_purchase()

            elif cmd == "sale":
                self.do_sale()

            elif cmd == "account":
                self.show_account()

            elif cmd == "list":
                self.list_warehouse()

            elif cmd == "warehouse":
                self.show_product()

            elif cmd == "review":
                self.do_review()

            elif cmd == "end":
                print("Saving data...")
                self.save_data()
                print("Goodbye!")
                break

            else:
                print("Unknown command.")


# ============================================================
# ENTRY POINT
# ============================================================

print(">>> File loaded")

if __name__ == "__main__":
    print(">>> Inside main block")
    system = AccountingSystem()
    print(">>> After creating system")
    system.run()
