message = "Hello"
print(message)

message = message + "World"
print(message)

# Integers
counter = 2
print(counter)

# Floating-points
weight_sum = 10.5
print(weight_sum)

# Strings
message1 = 'Hello world'
print(message1)
message2 = "Hello world"
print(message2)
message3 = '''
Hello
world
123
python
:)
'''
print(message3)

# Boolean (only True or False)
always_true = True
print(always_true)
always_false = False
print(always_false)

print()

# None
nothing_here = None
print(nothing_here)

print()

# Math operators
a = 1.5
b = 0.5
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print()

a = 2
b = 3
print(a ** b)  # 2 * 2 * 2
print(b % a)  # Remainder from division (e.g check if number odd/even)

print()

# Compairing objects
var1 = 5
var2 = 10
print(var1 == var2)
print(var1 != var2)
print(var1 < var2)
print(var1 <= var2)
print(var1 > var2)
print(var1 >= var2)

print()

# Logical operators
# OR <- at least one True
print(True or True)
print(True or False)
print(False or True)
print(False or False)

print()

# AND
print(var1 > 4 and var1 < 8)
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print()

# NOT
print(not False)
print(not True)

print()

print(bool(-1))  # True
print(bool(1))  # True
print(bool(2))  # True
print(bool(0))  # False
print(bool(0.0))  # False
print(bool(0.1))  # True
print(bool(""))  # False
print(bool(" "))  # True
print(bool("smoething"))  # True
print(bool(None))  # False

print()

# checking variable type
a = "text"
print(type(a))

print(type(a) is str)
print(type(a) is not str)

print("1" + "2")
print(int("1") + int("2"))

print()

# Text operations
print("Hello" + " " + "world")
print("Hello" * 5)

var1 = "a"
var2 = 2

print("Text for %s formatting %i" % (var1, var2))  # deprecated

print("This is the {} program line, containing word {}".format(134, "hello"))

text = "Hello world"
print(f"This is my text {text}")

print()

# input from user
print("What's your name?")
user_name = input()
print(f"Your name is {user_name}")

age = int(input("How old are you?"))
age_after_10_years = age + 10
print(f"You are {age} years old, in 10 years you will be {age_after_10_years} years old")

# additional text formatting
print("My favourite book is \"Harry Potter\" J.K. Rowling")  # Escape character
print("My favourite book is 'Harry Potter' J.K. Rowling")



