"""
    Expense
    John -> Credit Card
    Month 1   10000
              10% interest
              -> bill -> 11000

    Month 2   8000

    Month 3   9000

    Clear Bill
    John can pay no more than 3000(example)

    prediction -> in which month his bill will be all clear

    # CASE 1
    John expense in 1st Month
    Month 1   10000
              10%
              11000
    Month 2   3000
    Month 3   3000
    Month 4   3000
    Month 5   2000

    # CASE 2
    John expense in 1st Month
    Month 1   10000
              10%
              11000
    Month 2   5000
              10%
              5500
              ----
              16500

              3000
    Month 3   3000
    Month 4   3000
    Month 5   2000

    1. Enter the fixed minimum payment amount (installment)
    2. to make an expense -> month will be taken care by algo
    3. to make a payment (fixed payment)
        give the forecast of the month where the bill will become 0


"""