# 1. Number of pieces (piece price x number of pieces ordered)
# 2. Number of packages (package price * (number of ordered items / number of items in a package rounded up))
# 3. Quantity + extra extra % loss on trimmings, cut corners etc.
from math import floor

products = {
    "paint_can": {"price": 60},  # Product with art price
    "paint_brush": {"price": 60},  # Product with art price
    "floor_tiles_white": {"price": 120, "size": 15},  # Product with a price calculated according to packages
    "floor_tiles_black": {"price": 140, "size": 20},  # Product with a price calculated according to packages
    "planks": {"price": 80, "loss": 0.1, "unit": "meters"},  # Product with price per quantity
    "concrete": {"price": 60, "loss": 0.05, "unit": "kilograms"}  # Product with price per quantity
}

products_piece = {"paint_can", "paint_brush"}
products_pack = {"floor_tiles_white", "floor_tiles_black"}
products_amount = {"planks", "concrete"}


# functions to ask about quantity / number of products
def piece_or_pack_ask():
    print("Enter number of pieces")
    return int(input())


def amount_ask(unit_name):
    print("Enter quantity ({})".format(unit_name))
    return floor(int(input()))


# functions to calculate the price
def price_piece(price, quantity):
    return price * quantity


def price_pack(price, pack_size, pieces):
    packs = int((pieces + pack_size - 1) / pack_size)
    return packs * price


def price_amount(price, loss, quantity):
    return price * quantity * (1 + loss)


# functions to print confirmation
def piece_print(quantity):
    print("Ordered {} quantity".format(quantity))


def pack_print(quantity, pack_size):
    packs = int((quantity + pack_size - 1) / pack_size)
    print("Ordered {} the number of packages".format(packs))


def amount_print(quantity, unit):
    print("You ordered {} ({})".format(quantity, unit))


total_price = 0
while True:
    print("Enter a product name or a blank line if you want to end")
    product = input()
    if not product:
        break
    if product not in products:
        print("Wrong product name")
        continue
    # Let's ask about the order quantity
    if product in products_piece or product in products_pack:  # Product with art price #Product with a price calculated according to packages
        quantity = piece_or_pack_ask()
    if product in products_amount:  # Product with price per quantity
        quantity = amount_ask(products[product]["unit"])
    # Print the confirmation
    if product in products_piece:  # Product with art price
        piece_print(quantity)
    if product in products_pack:  # Product with a price calculated according to packages
        pack_print(quantity, products[product]["size"])
    if product in products_amount:  # Product with price per quantity
        amount_print(quantity, products[product]["unit"])
    # Let's add the price
    if product in products_piece:  # Product with art price
        total_price += price_piece(products[product]["price"], quantity)
    if product in products_pack:  # Product with a price calculated according to packages
        total_price += price_pack(products[product]["price"], products[product]["size"], quantity)
    if product in products_amount:  # Product with price per quantity
        total_price += price_amount(products[product]["price"], products[product]["loss"], quantity)

print("Total order cost {}".format(total_price))