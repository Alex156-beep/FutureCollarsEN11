# Task: Check if a number is even or odd

# Ask the user for an integer
number = int(input("Enter an integer: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

# OR Task 1

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Task 2: Find the largest of three numbers

# Ask the user for three numbers
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Find the largest number
largest = max(a, b, c)

# Print the result
print(f"The largest number is {largest}.")

# Task 3: Sum of numbers from 1 to n

# Ask the user for a number n
n = int(input("Enter a number: "))

# Calculate the sum of numbers from 1 to n
total = sum(range(1, n + 1))

# Print the result
print(f"The sum of numbers from 1 to {n} is {total}.")

# Task 4: Count characters in a sentence (without spaces)

# Ask the user for a sentence
sentence = input("Enter a sentence: ")

# Remove spaces and count characters
count = len(sentence.replace(" ", ""))

# Print the result
print(f"The sentence has {count} characters (excluding spaces).")

# Task 5: Guess the number

import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Initialize guess variable
guess = 0

# Keep asking until the user guesses correctly
while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed it!")

