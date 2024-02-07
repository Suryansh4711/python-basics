# List  Comprehension: the consice way to create a list
# [Expression for i in seq if condition]

# method - 1
# lst = [30, 23, 15, 67]
# out = []
# for i in lst:
#     out.append(i-2)
# print(out)

# method - 2 (list Comprehension)
# lst=[30, 23, 15, 67]
# out=[i-2 for i in lst]
# print(out)

# modulus fuction type
# lst=[30, 23, 15, 67]
# out=[i**2 for i in lst if i%2==0]
# print(out)

# read the space seperated integer array from the user
# out=[int(i) for i in input().split() ]
# print(out)

# generator object
# lst= [4, 6, 8]
# print(i-2 for i in lst)

# lst = [(), (), (45, ), ([],), (34, 6, 8), (), ('',)]
# for i in lst:
#     if len(i) == 0:
#         lst.remove(i)
# print(lst)

# lst = [(), (), (45, ), ([],), (34, 6, 8), (), ('',)]
# for i in lst:
#     if i == ():
#         lst.remove(i)
# print(lst)

# lst = [(), (), (45, ), ([],), (34, 6, 8), (), ('',)]
# out=[i for i in lst if i]
# print(out)

# names = ["pragyan", "kartokay", "uday", "parth"]
# out=[i for i in names if print(i)]
# print(out)

# generator expression
# kp=(34,54,55,0,100)
# tp=tuple(float(i) for i in kp)
# print(tp)

# lst=[4, 6, 8]
# new_lst=[1, 2, *lst, 34]
# print(new_lst)

# # OR

# lst1='Hello'
# new_lst1=[1, 2, *lst1, 34]
# print(new_lst1)

# u=*range(1, 4),
# print(u, type(u))

*st, u=*range(1, 100),
print(u, type(u))