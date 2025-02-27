import heapq
import sys
I=sys.stdin.readline
n=int(I())
l=[]
t=list(map(int,I().split()))
for i,e in enumerate(t):
    heapq.heappush(l,(e,i+1))
t.insert(0,10**10)
for _ in range(int(I())):
    o=I().strip()
    if(o=='2'): 
        q=[]
        while l[0][0]!=t[l[0][1]]:
            v,i=heapq.heappop(l)
        print(l[0][1])
        continue
    a,i,v=map(int,o.split())
    t[i]=v
    heapq.heappush(l,(v,i))