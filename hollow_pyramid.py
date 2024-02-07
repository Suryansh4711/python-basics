row=10
val = 65
for i in range(1, row+1):
    for j in range(row-i):
        print(' ', end='')
    for j in range(2*i-1):
        if j == 0 or j == 2*i-2 or i == row:
            print('*', end = '')
        else:
            print(' ', end = '')
            
    print()