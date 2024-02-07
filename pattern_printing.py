n=5
for i in range(1, n+1):
      for r in range(2*i-1):
            print('*', end=' ')

      print()


for i in range(1, n+1):
      for j in range(n-(2*i-1)+1):
            print('*', end=' ')
      print()



for i in range(1, n+1,2):
      print("*"*i)
