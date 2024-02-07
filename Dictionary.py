prices={}
num_pairs=int(input("Enter the number of key-value pairs: "))

for x in range(num_pairs):
    key=input("Enter the key: ")
    value=int(input("Enter the value: "))
    prices[key]=value

print("Resulting dictionary: ")
print(prices)

total_cost=0
for price in prices.values():
    total_cost += price

print(f"The total cost of all the items is: {total_cost}")