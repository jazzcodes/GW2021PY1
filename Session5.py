"""
    if/else
    switch case
    shopping cart program
    search sort and filter
    introduction to functions
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
    },
    "BINGO": {
        "min": 599,
        "flat": 300,
    },
    "JUMBO": {
        "min": 1000,
        "discount": 0.30,
        "upto": 200
    },
}

amount = int(input("Enter Your Amount: "))
promo_code = input("Enter Your Promo Code: ")

if promo_code in promo_codes:
    print("Promo Code Valid")
    promo_code_info = promo_codes[promo_code]
    if "discount" in promo_code_info:
        print("We will offer a percentage discount")
        print("DISCOUNT in Percentage:", promo_code_info["discount"])

        if amount >= promo_code_info["min"]:
            discount = amount * promo_code_info["discount"]

            if discount > promo_code_info["upto"]:
                amount -= promo_code_info["upto"]
            else:
                amount -= discount
        else:
            print("Amount is Lesser. Please add items worth \u20b9",  (promo_code_info['min']-amount), "more")
    else:
        print("We will offer a flat discount")
        print("Flat DISCOUNT:", promo_code_info["flat"])

        if amount >= promo_code_info["min"]:
            amount -= promo_code_info["flat"]
        else:
            print("Amount is Lesser. Please add items worth \u20b9",  (promo_code_info['min']-amount), "more")
else:
    print("Promo Code Invalid")


print("PLEASE PAY \u20b9", amount)