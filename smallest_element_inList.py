# Question: find the smallest element in the list
# Problem Statement: Write a program to find the smallest element in the given list

# method-1:

# ls=[5, 4, -1, 0, 54]
# min_element=ls[0]

# for num in ls:
#     if num<min_element:
#         min_element=num
# print(f"The smallest element in the list is: {min_element}")

# method-2 using sort:

ls1=[1, 2, 6, 50, -50, -4, -10]

ls1.sort()

print("Smallest element in the given list is:", ls1[0])