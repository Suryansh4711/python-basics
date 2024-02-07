# Question: Find the Intersection (Common elemnts) of Two lists
# Problem Statements: Write a programe to find the common elemnts of the two lists

ls1=[1, 2, 3, 4, 5, 6, 7]
ls2=[3, 5, 5, 4, 8, 7, 2]
intersection=[]

for num in ls1:
    if num in ls2 and num not in intersection:
        intersection.append(num)

print(f"The intersection of the two lists is: {intersection}")