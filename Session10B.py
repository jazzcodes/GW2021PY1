# Strings in Python
johns_cafe_name = 'Johns Cafe Shop'
print(johns_cafe_name, type(johns_cafe_name))
print(len(johns_cafe_name))
print(max(johns_cafe_name))
print(min(johns_cafe_name))

johns_cafe_name = 'John\'s Cafe Shop'
johns_cafe_name = "John's Cafe Shop"
johns_cafe_name = """---------------
Johns Cafe Shop
Have a sip with us
---------------
"""
print(johns_cafe_name)

# Raw Strings are Used with Regular Expressions :)
johns_cafe_name = r"Johns\nCafe Shop"
print(johns_cafe_name)

# Property -> Strings are IMMUTABLE
# Strings cannot be modified.
# Any manipulation on String will create a new String in Memory
names = "john, jennie, jim, JACK, joe"
new_names = names.upper()
print(names)
print(new_names)

capitalize_names = names.capitalize()
print(capitalize_names)

print(names.title())
print(names.swapcase())

# password = input("Enter Password: ").strip()
# password = input("Enter Password: ").rstrip()
# password = input("Enter Password: ").lstrip()
# print("password is:", password)

data = "00000000032500"
print(data.strip("0"))
print(data)

message = "No Internet Connectivity"
print(message.center(60))
print(message.ljust(60))
print(message.rjust(60))

print("545".rjust(10, '-'))
print("545".zfill(10))

quote = "search the candle rather than cursing the darkness"
print(quote.find("sing"))
print(quote.index("the"))
print(quote.rindex("the"))


names = "john, jennie, jim, jack, joe"
print(len(names)) # 28
print(names[len(names)-1])
# split_names = names.split()
split_names = names.split(", ")
print(split_names)

partitioned_names = names.partition("jim")
print(partitioned_names)

for ch in names:
    print(ch, end=" ~ ")

print()
print("names:", names.replace("john", "kohn"))

contacts = [
    "John",
    "George",
    "Harry",
    "Joe",
    "Joanna",
    "Kim",
    "Sim"
]

search_keyword = input("Search:  ")
print("SEARCH Keyword: ", search_keyword)


for contact in contacts:
    # if contact.lower().__contains__(search_keyword.lower()):
    if contact.lower().startswith(search_keyword.lower()): # endswith
        print(contact)

name = "John"
age = 20
email = "john@example.com"

print("Details for {} \n{} and {}".format(name, age, email))
print("Details for {0} \n{1} and {2}".format(name, age, email))
print("Details for {first} \n{y} and {any}".format(first=name, y=age, any=email))

bill_amount = 120.54311
print("Bill is: {0:.2f}".format(bill_amount))

name = "Fionna"