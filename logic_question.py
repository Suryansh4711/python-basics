x=int(input("Enter the starting number: "))
y=int(input("Enter the ending number: "))

for i in range(x, y+1):
    if i%2==0 and i%3==0:
        print(i, ": Good Student!")
    elif i%3==0:
        print(i, ": Student")
    elif i%2==0:
        print(i, ": Good")
    else:
        print(i)