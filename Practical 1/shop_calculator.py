prices = []
total = 0
amount = int(input("Number of items: "))
while amount <= 0:
    print("Invalid number of items!")
    amount = int(input("Number of items: "))
for i in range(amount):
    price = float(input("Price of item: "))
    prices.append(price)
for count in range(len(prices)):
    total = total + prices[count]
print(f"Total price for {amount} items is ${total:.2f}")
