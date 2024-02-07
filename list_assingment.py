my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#access and print the element at index 3
print(my_list1[3])

#access and print the last eement of list
print(my_list1[-1])

#access and print a sublist containing elements from index 1 to 4(inclusive)
print(my_list1[1:4])

#change the value at index 2 to 10
my_list1[2]=10
print(my_list1)

#append the value 20 to the end of the list
my_list1.append(20)
print(my_list1)

#remove the element at index 0
del my_list1[0]
print(my_list1)

#insert the value 5 at index 1
my_list1.insert(1, 5)
#print the final list
print(my_list1)