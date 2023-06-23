# n = int(input())
# for i in range(1, n+1):
#     print('*' * (n+1 - i))

# for i in range(2, n+1):
#     print('*' * i)
    
n = int(input())
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print('*',end="")
    print()
for i in range(1,n):
    for j in range(1,i+2):
        print('*',end="")
    print()
