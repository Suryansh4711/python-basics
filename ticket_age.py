age=int(input("enter your age:- "))
if age<=3:
     ticket="free"
elif age<=12 and age>=4:
     ticket=10
elif age<=17 and age>=13:
    ticket=15
else:
    ticket=20
print(f"the price of the ticket is {ticket}$")