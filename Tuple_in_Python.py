# Python Tuples
# Tuples are identical to lists in all respects, except for the following properties:
# 1. Tuples are defined by enclosing the elements in parantheses(()) instead of square brackets([]).
# 2. Tuples are immutable.

# Creating Tuple
# A tuple is created by placing all the items inside parantheses() and seperated by (,).
# Sometimes parantheses are optional

# A tuple can have any number of items and they may be of 
# different types (integer, float, list, string etc.)

# Intialization Empty tuple
# t = ()
# t = tuple() #constructor
# print(t, type(t)) 

# Intialising Tuple
# t=tuple('hello')
# print(t)

#
# *t, p, y = 'hello'
# print(f'{t=}')
# print(f'{p=}')
# print(f'{y=}')

# map():
# ls = '34 56 1 2 0 8'.split() #['34', '56', '1', '2', '0', '8']
# print(ls)

# #map()input
# ld=input().split()
# print(ld)

#map()input and map function
# ls1=input().split()
# ls2=map(int, ls1)
# print(ls1)
# print(ls2)

# # map()
# obj = list(map(int, input().split()))  *****important*****

# mytuple=("stud", "stud1", "stud2", "stud3")
# print(mytuple)
# print(len(mytuple))
# print(type(mytuple))

# tuple1=(1,2,3,4,5,6)
# tuple2=(11,12,5,6,8)
# print(tuple1, tuple2)

# tp1=(1,2,3,5,11,0,9)
# tp2=("a","b","c")
# tp3=tp1+tp2
# print(tp3)
# print(tp1*2)
# print(tp2*2)

# s=("s1","s2","s3","s4")
# 1. for x in s:
#     print(x)

# 2. for y in range(len(s)):
#     print(y)

# 3. i=0
#    while i<len(s):
#       print(s[i])
#       i+=1


# list in tuple
# s=("s1","s2","s3","s4","s5","s6","s7","s8")
# print(s[2])
# print(s[2:5])
# print(s[2: ])
# print(s[ :6])
# print(s[-4:-1])
# print(s.count("s5"))
# print(s.index("s4"))

# tuple modification
# x=("e1","e2","e3")
# y=list(x)
# y[1]="e4"
# z=tuple(y)
# print(z)

# b=list(x)
# b.append("e5")
# t=tuple(b)
# print(t)

# unpacking of tuple
# students=("s1","s2","s3")
# (one, two, three)=students
# print(one)  #s1
# print(two)  #s2
# print(three)  #s3

# employees=("e1","e2","e3","e4")
# (one, *two)=employees
# print(one)   # e1
# print(two)   #['e2', 'e3', 'e4']

