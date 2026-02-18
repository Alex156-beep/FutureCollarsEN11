firstname = "Marek"
if firstname[-1] == "a":
    gender = "f"
else:
    gender = "m"

gender = "f" if firstname[-1] == "a" else "m"  # Shortened way

list_a = ["Adam", "ewa", "John", "jack", "anna", "Jim"]
list_b = []
for firstname in list_a:
    list_b.append(firstname.capitalize())
print(list_b)

# [<new item> for <item> in <list>]
list_c = [firstname.capitalize() for firstname in list_a]  # Shortened way
print(list_c)

list_b = []
for firstname in list_a:
    if firstname != firstname.capitalize():
        list_b.append(firstname.capitalize())

print(list_b)

# [<new item> for <item> in <list> <if condition>]
list_c = [firstname.capitalize() for firstname in list_a if firstname != firstname.capitalize()]
print(list_c)

set_a = {firstname.capitalize() for firstname in list_a if firstname != firstname.capitalize()}
print(set_a)

# firstname is key : firstname.capitalize() is value
dict_a = {firstname: firstname.capitalize() for firstname in list_a}
print(dict_a)

# pip install pytests <- install new package
# pip freeze <- list all dependencies
# pip freeze > requirements.txt <- create file with dependencies
# pip install -r .\requirements.txt <- install dependencies from file

# BE CAREFUL WHEN USING THIS COMMANDS
# recommend to copy .venv directory before
# deactivate - deactivate your venv
# .\.venv\Scripts\activate - activate venv
# python.exe -m venv venv2 -generate new venv