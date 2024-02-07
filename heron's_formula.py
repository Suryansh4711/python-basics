# Code of area of triangle using Heron's Formula:
a=float(input("enter the first side\n"))
b=float(input("enter second side\n"))
c=float(input("enter third side\n"))
s=(a+b+c)/2
area_s = (s*(s-a)*(s-b)*(s-c))**1/2
print(f"the area of a triangle by Heron's formula is: {area_s}")