n=int(input("enter the first natural numbers(n)\n"))
sum_of_even_numbers=0
sum_of_odd_numbers=0

for i in range(1, n+1):
    if i%2==0:
      sum_of_even_numbers+=i
    else:
      sum_of_odd_numbers+=i

print(f"the sum of {n} natural even numbers is: {sum_of_even_numbers}")
print(f"the sum of {n} natural odd numbers is: {sum_of_odd_numbers}")