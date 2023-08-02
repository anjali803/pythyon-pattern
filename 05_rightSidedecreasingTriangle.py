'''
'''
n = 5 
for i in range(n):
    
    for j in range(i):
        print(" ",end=" ")
        if (i==0 and j == n):
            print("*",end=" ")
    for k in range(n-i):
        print("*",end=" ")
    print()