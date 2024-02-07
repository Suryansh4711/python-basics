# Question 7: Remove Duplicate from the list
# Problem Statement: Write a Program to remove the duolicate elements from a list
ls1=[1, 2, 2, 3, 3, 5, 5, 8, 4]
ls=[]
for num in ls1:
    if num not in ls:
        ls.append(num)

print(f"The list after removing duplicates is: {ls}")