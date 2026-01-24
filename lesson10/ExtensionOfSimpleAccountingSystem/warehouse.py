class Manager:
    def __init__(self):
        self.balance = 0
        self.warehouse = {}
        self.history = []
        self.actions = {}

    # ================= DECORATOR =================

    @staticmethod
    def record_action(name):
        def decorator(func):
            def wrapper(self, *args, **kwargs):
                result = func(self, *args, **kwargs)
                self.history.append(name)
                return result
            return wrapper
        return decorator

    # ================= ASSIGN =================

    def assign(self, name, method):
        self.actions[name] = method

    # ================= ACTIONS =================

    @record_action("balance")
    def change_balance(self, amount):
        self.balance += amount
        print("Balance:", self.balance)

    @record_action("purchase")
    def purchase(self, product, price, quantity):
        cost = price * quantity
        if self.balance < cost:
            print("Not enough money")
            return
        self.balance -= cost
        self.warehouse[product] = self.warehouse.get(product, 0) + quantity

    @record_action("sale")
    def sale(self, product, price, quantity):
        if self.warehouse.get(product, 0) < quantity:
            print("Not enough product")
            return
        self.warehouse[product] -= quantity
        self.balance += price * quantity

    @record_action("list")
    def list_warehouse(self):
        print("Warehouse:")
        for product, qty in self.warehouse.items():
            print(product, qty)

    @record_action("review")
    def review(self):
        print("History:")
        for action in self.history:
            print(action)


# ================= PROGRAM TEST =================

manager = Manager()

# Assign commands
manager.assign("balance", manager.change_balance)
manager.assign("purchase", manager.purchase)
manager.assign("sale", manager.sale)
manager.assign("list", manager.list_warehouse)
manager.assign("review", manager.review)

# Simulate operations

manager.actions["purchase"]("apple", 2, 100)
manager.actions["sale"]("apple", 3, 20)
manager.actions["list"]()
manager.actions["review"]()