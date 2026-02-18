class Product:
    counter = 0

    # price_sum = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = Product.counter
        Product.counter += 1
        # Product.price_sum += price

    def __str__(self):
        return self.name

    def get_price(self, qty):
        return self.price * int(qty)