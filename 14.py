n = int(input())
inc=0
for i in range(n//2,-(n//2+1),-1):
    inc = inc+1
    for j in range(1,n//2-abs(i)+1):
        print(end=" ")
    for k in range(1,2*abs(i)+2):
        print(chr(64+inc),end="")
    print()