num=int(input("enter the number to get desired multiplication table\n"))
if num<=0:
    print("invalid")
else:
 for i in range(1,11):
    m=num*i
    print(f"{num}x{i}={m}")