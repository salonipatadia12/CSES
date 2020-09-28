# n,m,k = map(int,input().split())
# desired = list(sorted(map(int,input().split())))
# size = list(sorted(map(int,input().split())))
# i=0
# j=0
# count=0
# while i<len(desired) and j<len(size):
#     if abs((desired[i]-size[j]))<=k:
#         i+=1
#         j+=1
#         count=count+1
#         # print(count)
#     else:
#         if(size[j]>desired[i]+k):
#             i+=1
#         else:
#             j+=1
# print(count)
#
#
#

import sys

num = [int(x) for x in sys.stdin.read().split()]

n, m, k = map(int, input().split())
want = num[3:n + 3]
avail = num[n + 3:]

i=0
j=0
count=0
while i<len(want) and j<len(avail):
    if abs((want[i]-avail[j]))<=k:
        i+=1
        j+=1
        count=count+1
    else:
        if(avail[j]>want[i]+k):
            i+=1
        else:
            j+=1
print(count)
