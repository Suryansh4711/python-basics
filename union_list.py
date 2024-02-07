# Question 1: find the union (all unique elements from both the lists) of two lists
# Problem Statement: Write a program to find the union of the two lists

ls1=[1, 2, 3, 8, 5, 7]
ls2=[1, 2, 5, 8, 10, 6]
union_list=[]

for num in ls1+ls2:
    if num not in union_list:
        union_list.append(num)

print(f"The union of the two list is: {union_list}")