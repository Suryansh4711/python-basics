# Question: remove specific element from a list
# Problem Statement: Write a program to remove a specific element from a list

ls1=[1, 2, 3, 4, 0]
element_to_remove = 2

nls=[item for item in ls1 if item != element_to_remove]

print(f"The list after removing {element_to_remove} is: {nls}")