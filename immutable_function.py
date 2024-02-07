# Immutable data Types:

def modify_int(x):
    x += 10
    print('Inside the function:', x)

num = 5
modify_int(num)
print("This is not inside the function:", num)

def modify_string(s):
    s += "World!"
    print("Inside the function:", s)

greetings = "Hello"
modify_string(greetings)
print("Outside the function:", greetings)

def modify_tuples(t):
    # tuples are immmutable, so creating a new tuple
    t += (4, 5)
    print("Inside the function:", t)

coordinates = (1, 2, 3)
modify_tuples(coordinates)
print("Outsid the function:", coordinates)
