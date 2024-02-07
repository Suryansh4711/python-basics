#assingment1: sum of first N natural number
n=int(input("enter a positive integer (N): "))
sum_of_numbers=0

for i in range(1, n+1):
    sum_of_numbers += i    #sum_of_number = sum_of_number + 1

print(f"the sum of first natural numbers is : {sum_of_numbers}")