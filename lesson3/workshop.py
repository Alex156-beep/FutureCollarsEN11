from lesson3.main import firstname, lastname

my_list = ["John", "Mark", "Will", "John", "John", "Angelina", "Jack", "Jim", "John"]

# Find index of all Johns
print(my_list.index("John"))
print(my_list.index("John", 1))
print(my_list.index("John", 4))
print(my_list.index("John", 5))

print()
print("Searching from: 0")
idx = my_list.index("John", 0)
print(idx)
while idx < len(my_list) - 1:  # -1 because length is 9, but the last position is 8
    # print("Searching from: {}".format(idx+1))
    idx = my_list.index("John", idx + 1)
    print(idx)

# Print collection without duplicates
print(set(my_list))

# Calculate how many duplicates we have
print(len(my_list))
print(len(set(my_list)))

print(len(my_list) - len(set(my_list)))

# Printing dictionary
fullnames = {
    1: ("John", "Doe"),
    2: ("Marek", "Wisniewski"),
    3: ("William", "Smith")
}
#k = keys, v = values
for k, v in fullnames.items():
    firstname, lastname = v
    print(f"Number{k}. {firstname} {lastname}")
