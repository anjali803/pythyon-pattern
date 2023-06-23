'''
   A
  B C
 D   E
FGHIJKL '''

    
n = int(input())
k=ord("A")
for i in range(1,n+1):
    for j in range(1,2*n):
        if(i==n or i+j==n+1 or j-i==n-1):
            print(chr(k),end="")
            k=k+1
        else:
            print(end=" ")
    print()
    