#Question: Reverse a list.
# Problem statement: Write a program too reverse a given list.
my_list = []

num_items = int(input("Enter the number of items to add to the lists: "))

for i in range(num_items):
    item = int(input(f"Enter item {i+1}: "))
    my_list.append(item)

print("Final list:", my_list)
# my_list = [1, 2, 3, 4, 5]
reversed_list = []

for i in range(len(my_list) -1, -1, -1):
    reversed_list.append(my_list[i])

print(f"The reversed list is: {reversed_list}")