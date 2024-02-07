# merge to list
# method:1
# ls1=[1,2,3,5]
# ls2=[2,5,6,4]
# ls=ls1 + ls2

# print(f"the new list is: {ls}")

# method;2
# ls1=[1, 2, 3, 5, 6]
# ls2=[5, 'b', 'c']

# for num in ls2:
#     ls1.append(num)

# print(ls1)

# method:3
ls1=[1,3,5]
ls2=[6,2,4]

ls1.extend(ls2)
print(ls1)