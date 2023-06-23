'''
          0 
        1 0 1
      2 1 0 1 2
    3 2 1 0 1 2 3
  4 3 2 1 0 1 2 3 4
  
'''
n = int(input())
for i in range(1,n+1):
    for j in range(n-i+1):
        print(end="  ")
    for k in range(i,0,-1):
        print(k-1,end=" ")
    for w in range(2,i+1):
        print(w-1,end=" ")
    print()