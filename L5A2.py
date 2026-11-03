actual_price=float(input("Please enter the price you bought it for: "))
sale_price=float(input("Please enter the amount you sold it for: "))

if sale_price>actual_price:
    amount=sale_price-actual_price
    print("You've made a profit of - {0}".format(amount))
else:
    print("Sorry no profit")