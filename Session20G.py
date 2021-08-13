# Java Script Object Notation
# Universal Standard to Share data in REST Architecture | REST (Representational State Transfer)

import json

covid_case = {
    "state": "Punjab",
    "confirmed": 344241,
    "active": 1233,
    "vaccinated": [13232, 2101]
}

print(covid_case, type(covid_case))

# we can convert dictionary to JSON
# JSON is just a string representation of Dictionary

json_data = json.dumps(covid_case)
print(json_data, type(json_data))

# json_data = str(covid_case)
# print(json_data, type(json_data))

dictionary_data = json.loads(json_data)
print(dictionary_data, type(dictionary_data))