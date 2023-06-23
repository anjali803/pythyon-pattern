n = int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(end=" ")
    x=i-1
    for k in range(1,2*i):
        if(k<=i):
            x=x+1
        else:
            x=x-1
        print(x,end="")
  
    print()

