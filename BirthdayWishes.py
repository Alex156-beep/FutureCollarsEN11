recipient_name = input("What is recipient's name?")
year_of_birth = int(input("Enter the year of birth:"))
age = 2025 - year_of_birth
text = input("Personalized message:")
sender_name = input("What is sender's name?")

print()

print(f" {recipient_name}, let's celebrate your {age} years of awesomeness!")
print(f"Wishing you a day filled with joy and laughter as you turn {age}!")
print(f"{text}")
print(f"With love and best wishes,")
print(f"{sender_name}")

