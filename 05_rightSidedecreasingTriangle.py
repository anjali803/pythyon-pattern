'''
'''
n = 5 
for i in range(n):
    for j in range(1,i+1):
        print("*",end="")
    for k in range(n-1):
        print(" ",end=" ")
    print()