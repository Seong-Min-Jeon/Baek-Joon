import sys
import heapq
ip=sys.stdin.readline
n,k=map(int,ip().split())
l=[[0] for _ in range(11)]
for _ in range(n):
    a,b=map(int,ip().split())
    heapq.heappush(l[a-1],-b)
for _ in range(k):
    for i in range(11):
        a=heapq.heappop(l[i])
        if(a!=0): a+=1
        heapq.heappush(l[i],a)
s=0
for i in range(11):
    s+=heapq.heappop(l[i])
print(-s)