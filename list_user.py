#take the input from the user and add the items in the list and print the final list
my_list = [1, 5, 5, 6, 8, 7, 8, 9, 11]
user_list = int(input("enter the integer list of your choice: "))

for i in range(user_list):
    my_list.append(user_list)

print(my_list)