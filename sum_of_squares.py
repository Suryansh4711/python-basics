# 1. Write a function that takes a list of numbers and returns the sum of the squares of all the numbers. Try it using a for loop first, then
def sum_of_squares(numbers):
    sqaures = [number ** 2 for number in numbers]
    return sum(sqaures)


print(sum_of_squares([1,2,3,4,5]))