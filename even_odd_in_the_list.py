# Question: Countb Even and Odd numbers in a list
# Problem Statement: Write a program to count the numbers of even and odd numbers in a list

list_1=[1, 3, 5, 6, 8, 4, 9]
count_odd=0
count_even=0

for num in list_1:
    if num%2==0:
        count_even += 1
    else:
        count_odd += 1

print(f"the number of even integers in the list is: {count_even}")
print(f"the number of odd integers in the list is: {count_odd}")