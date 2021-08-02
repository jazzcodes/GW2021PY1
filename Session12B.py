"""
    Regular Expressions
    Flexible Pattern Matching Technique
"""

import re

regex = re.compile("\s+")
print(regex, type(regex))

quote = "search    the candle rather than cursing the darkness"
result = regex.split(quote)
print(result)

contact_names = ["      ", "john", "jennie   ", "   george  "]
for name in contact_names:
    if regex.match(name): # will match from beginning
        print("Pattern Matched For", name)
    else:
        print("Pattern NOT Matched For", name)

regex = re.compile(""
                   "")
result = regex.split(quote)
print(result)


data = regex.search(quote)
print(data)
print(data.start())

new_quote = quote.replace('the', 'will')
print("quote:", quote)
print("new_quote:", new_quote)

# new_quote = regex.sub("will", quote)
# print(new_quote)
print()

email = "john@example.com"
flag = True
for i in range(len(email)):
    if email[0] == '@':
        flag = False
    if email[0] == '.' or email[1] == '.':
        flag = False

email_regex = re.compile("\w+@\w+\.[a-z]{3}")

# message = input("Write a message")
# print("You Entered:", message)
# result = email_regex.findall(email)
# print(result)

message = "This is a good day. is it going to rain ?"
regex = re.compile("is")
results = regex.findall(message)
print(results)

message = "Please Pay $100 Awesome."
# regex = re.compile("\$[0-9][0-9][0-9]")
regex = re.compile("\$\w+")
print(regex.findall(message))

message = "I have been vaccinated 2 times. I am 12 years old. i feel more safer"
regex = re.compile('[0-9]')
result = regex.findall(message)
print(result)

regex = re.compile("[A-Z][0-9]")
data = "108AB, PB, HP, A6, 55"
results = regex.findall(data)
print(results)

message = "I have a 2 wheeler vehicle. Registration Number is PB10AL2937"
pattern = r"[A-Z]{2}\d{2}[A-Z]{2}\d{4}"
regex = re.compile(pattern)
result = regex.findall(message)
print(result)
