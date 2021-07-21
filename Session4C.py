"""
    if/else
"""

promo_codes = {
    "NOCOOKING": {
        "min": 159,
        "discount": 0.50,
        "upto": 100
    },
    "WELCOMEPTM": {
        "min": 299,
        "flat": 75,
    }
}

amount = int(input("Enter Your Amount: "))
promo_code = input("Enter Your Promo Code: ")

print("AMOUNT: \u20b9", amount)
print("PROMO CODE:", promo_code)

# Regular if/else
# if promo_code in promo_codes:
#     print("We will give discount")
# else:
#     print("Invalid Promo Code")

# Nested if/else
if promo_code in promo_codes:
    print("Promo Code Valid")
    promo_code_info = promo_codes[promo_code]
    if "discount" in promo_code_info:
        print("We will offer a percentage discount")
        print("DISCOUNT in Percentage:", promo_code_info["discount"])
    else:
        print("We will offer a flat discount")
        print("Flat DISCOUNT:", promo_code_info["flat"])
else:
    print("Promo Code Invalid")
