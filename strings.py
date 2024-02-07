a = input("enter the word:\n")
digit = ""
alphabets = ""
count_al = 0
count_nu = 0
count_sc = 0
count_sp = 0
for i in range(len(a)):
    if (a[i].isalpha()):
        alphabets += a[i]
        count_al += 1
    elif (a[i].isdigit()):
        digit += a[i]
        count_nu += 1
    elif (a[i].isspace()):
        count_sp += 1
    else:
        count_sc += 1
print(f"the alphabets are: {alphabets}")
print(f"the digits are: {digit}")
# print(f"the alphabets in the given string is= {count_al}")
# print(f"the no. of digits in the given string is= {count_nu}")
# print(f"the spaces in the string is= {count_sp}")
# print(f"the special characters in the given string is= {count_sc}")
# print(f"reversed string = {a[::-1]}")
