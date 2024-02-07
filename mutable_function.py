# Mutable data type:

def modify_list(lst):
    lst.append(4)
    lst[0] = 99
    print("Inside the function:", lst)

numbers = [1, 2, 3]
modify_list(numbers)
print("Outside the function:", numbers)


def modify_dict(d):
    d['new_key'] = 'new_value'
    print("Inside the function:", d)

my_dict = {'key1': 'value1', 'key2': 'value2'}
modify_dict(my_dict)
print("outside the function:", my_dict)

def modify_set(s):
    s.add(4)
    print("Inside the function:", s)

my_set = {1, 2, 3}
modify_set(my_set)
print("Outside the function", my_set)