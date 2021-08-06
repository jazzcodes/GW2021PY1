# map, filter, reduce
from functools import reduce

product_prices = [2000, 2500, 1500, 6000, 7000, 8000, 11000, 12000]


def calculate_discount(amount, discount=0.50):
    return amount - (amount*discount)


cal_dis_lambda = lambda amount, discount=0.50: amount - (amount*discount)


for price in product_prices:
    print("Original Price:", price)
    # print("Discounted Price:", price-(0.50*price))
    # print("Discounted Price:", calculate_discount(price, 0.50))
    print("Discounted Price:", cal_dis_lambda(price, 0.50))
    print()

# result = map(calculate_discount, product_prices)
# result = list(map(calculate_discount, product_prices))

# result = list(map(cal_dis_lambda, product_prices))

# map function will do mapping
result = list(map(lambda amount: amount - (amount*0.50), product_prices))
print("result is:", result)

result = list(filter(lambda amount: amount > 5000, product_prices))
print("result is:", result)

shopping_cart = [1000, 2000, 2500]
print("shopping_cart to begin with:", shopping_cart)
shopping_cart = list(map(lambda amount: amount-(amount*0.50), shopping_cart))
print("shopping_cart now:", shopping_cart)

amount_to_pay = reduce(lambda x, y: x+y, shopping_cart)
print("amount_to_pay for your cart", amount_to_pay)
