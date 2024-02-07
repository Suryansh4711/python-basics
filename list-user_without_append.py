num_elements = int(input("Enter the numbers of elemnts to add to the list: "))
Original_list = [0] * num_elements
print("Original list:", Original_list)

for i in range(num_elements):
    element = int(input(f"Enter the element : "))
    # element = input(f"Enter element (i+1):")
    Original_list= element

print("finally the list;", Original_list)