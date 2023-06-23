   
# n = int(input())
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end="")
#     print()
# for i in range(2,n+1):
#     for j in range(i-1):
#         print(" ",end="")       
#     for j in range(n-i+1):
#          print("*",end="")
#     print()

# mirror img varubol ann asb edukunath
n = int(input())
for i in range(n-1,-n,-1):
    for j in range(1,abs(i)+1):
        print(" ",end="")
    for k in range(1,n-abs(i)+1):
        print("*",end="")
    print()
'''
*
**
***
****
***
**
*
'''
