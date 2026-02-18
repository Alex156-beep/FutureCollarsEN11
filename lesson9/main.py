import json

from lesson9.Product import Product
from lesson9.Product2 import Product as Product2, MBRProduct

print(Product.counter)
p1 = Product("a1", 100)
print(Product.counter)
p2 = Product("a2", 200)
print(Product.counter)
p3 = Product("a3", 300)
print(Product.counter)

print(p1)
print(p1.id)
print(p2)
print(p2.id)
print(p3)
print(p3.id)

p4 = Product("a4", 400)

print(Product.counter)
print(p4.id)

# print(Product.price_sum)

# Execute method using class name
print(Product.get_price(p1, 2))  # p1 -> self
print(p1.get_price(2))

print()
print()
print()

mbrp = MBRProduct("mbr", 100, 10)
print(mbrp.get_price(9))
print(MBRProduct.get_price(mbrp, 9))  # The same as line above

# ===============================Exceptions===============================
try:
    integer_val = int(input("Provide number: "))
except ValueError as e:
    integer_val = 0
    print(e)

print(integer_val)

try:
    integer_val1 = json.loads("{a")  # Stopping execution of all block
    integer_val2 = int(input("Provide number: "))
except json.decoder.JSONDecodeError as e:
    integer_val1 = 0
    print(e)
except ValueError as e:
    integer_val2 = 0
    print(e)

try:
    integer_val1 = json.loads("{a")
except json.decoder.JSONDecodeError as e:
    integer_val1 = 0
    print(e)

try:
    integer_val2 = int(input("Provide number: "))
except ValueError as e:
    integer_val2 = 0
    print(e)