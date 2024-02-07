# A function is a block of code which only runs when it is called.

# you can pass data, known as parameters into a function.

# A function can return data as a result.


# In python a function is defined using the def keyword.
def my_fnction():
    print("Hello from a function")

my_fnction() #to call a function, use the function name followed by parenthesis.


print()


# Funtion with parameters
def my_function1(fname):
    print("My name is:- " + fname)

my_function1("Ram")
my_function1("Rahul")
my_function1("Shyam")

def arguments(fname, lname):
    print(fname + " " + lname)

arguments("Rahul", "Das")


def my_food(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_food(fruits)

# Arbitrary arguments *args
def my_funtion(*kids):
    print("The youngest child is:- " + kids[1])

my_funtion("Emily", "Tobias", "Linus")

# return keyword
def my_function(x):
    return 5*x

print (my_function(3))
print (my_function(5))
print (my_function(9))