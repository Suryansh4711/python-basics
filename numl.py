num1=float(input("enter first number\n"))
num2=float(input("enter second number\n"))
if num1<1 or num2<1:
 print("invalid")
elif num1<num2:
  print(num1,"is the smallest and",num2,"is the largest")
elif num1>num2:
  print(num1,"is the largest and",num2,"is the smallest")
elif num1==num2==4:
  print("valid")
