
'''
    A 
   A B
  A B C
 A B C D
A B C D E   '''

n = int(input())
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for k in range(0,i+1):
        print(chr(65+k),end=" ")
    print()
    