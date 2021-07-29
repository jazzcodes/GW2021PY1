# Dictionary
my_data = {}
print(my_data, type(my_data), len(my_data))

my_data = {101: "John", 201: "Fionna", 301: "Jack"}
print(my_data, type(my_data), len(my_data))
print(min(my_data))
print(max(my_data))

# print(my_data[201])
# print(my_data[501]) -> KeyError

print(my_data.get(201))
print(my_data.get(501))

# del my_data[101]
# my_data.pop(101)
# print(my_data)

pair = my_data.popitem()
print(pair)
print(my_data)

covid_cases = {}.fromkeys(["active", "confirmed", "recovered"], 0)
print(covid_cases)

covid_cases["active"] = 56345
covid_cases["confirmed"] = 2563
covid_cases["recovered"] = 762563

items = covid_cases.items()
print(items, type(items))

# for item in items:
for item in covid_cases.items():
    print(item[0], item[1])

keys = covid_cases.keys()
print("keys:", keys)

for key in keys:
    print(key, covid_cases[key])

# for idx, data in enumerate(covid_cases):
#     print(idx, data)

idx = 0
for key in keys:
    print(idx, key, covid_cases[key])
    idx+=1