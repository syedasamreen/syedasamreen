#innerloop
#outerloop
# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print('*',end = ' ')
#     print( )
#
#
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print('*',end = ' ')
#     print( )

##printing numbers
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print( )
#
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print( )
#
## drcreasing order
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j, end=' ')
#     print()
#
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j, end=' ')
#     print()
##continues number
# n=0
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(n, end=' ')
#         n= n+1
#     print()

##lrl

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end = ' ')
    for k in range(j-1, 0,-1):
            print(k,end= ' ')
    print()