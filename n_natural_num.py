def natural_num(n):
    return n*(n+1)//2

num=int(input("Enter the number: "))
print(f"The sum of {num} natural numbers is : {natural_num(num)}")
natural_num(num)