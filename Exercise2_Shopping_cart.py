item = input("What would you like to buy?: ")
price = float(input("what is the price? :"))
quantity = int(input("how many of the items do you want to buy?:"))
total_cost = price * quantity

print(f"The total cost of {quantity} {item}(s) will be Rs.{total_cost}")

