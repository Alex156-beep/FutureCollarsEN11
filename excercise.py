# Task 1
from main import user_name

name = "Aleksandra"
age = 18
print(f"Hi, my name is {name} and I am {age} years old")

# Task 2
a = 5
b = 8
sum_result = a + b
difference = a - b
product = a * b
quotient = a / b

print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)

# Task 3
address = "Warsaw, Flower Street 15"
rooms = 3
area = 75.5
print(f"My house is located at {address}, it has {rooms} rooms and an area of {area} square meters.")
print("My house is located at {}, it has {} rooms and an area of {} square meters.".format(address, rooms, area))

# Task 4
x = 10
y = 20
print(x)
print(y)

# x, y = y, x

temp = x
x = y
y = temp

print(x)
print(y)

# Task 5
integer_number = 12
float_number = 3.14
text = "Python"
boolean_value = True

print(type(integer_number))
print(type(float_number))
print(type(text))
print(type(boolean_value))

# Task 6
age = int(input("How old are you?"))
money = int(input("How much money do you have?"))
minimum_age = 18
ticket_cost = 30
result = age >= minimum_age and money >= ticket_cost
print(f"You can go to the movie -> {result}")

recipients_name = input("Alex")
year_of_birth = int(input("1995"))

