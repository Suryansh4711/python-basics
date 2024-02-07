num=int(input("enter the integer = "))
a=0
b=1
c=0
print(f"the fibonacci sequence is {a}")
if num <= 1000:
   for i in range(1, num+1):
      a = b
      b = c
      c = a+b
      print(f"the fibonacci sequence is {c}")