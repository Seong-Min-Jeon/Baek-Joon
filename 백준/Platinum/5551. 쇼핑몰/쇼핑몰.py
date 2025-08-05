import sys,heapq,math
I=sys.stdin.readline
n,m,k=map(int,I().split())
l=[[] for _ in range(n+1)]
t=set()
for i in range(m):
    a,b,d=map(int,I().split())
    l[a].append((b,d))
    l[b].append((a,d))
    t.add((a,b,d))
for _ in range(k):
    l[0].append((int(I()),0))
r=[1e9]*(n+1)
q=[(0,0)]
r[0]=0
while q:
    d,p=heapq.heappop(q)
    if(r[p]<d): continue
    for i,e in l[p]:
        if(d+e<r[i]):
            r[i]=d+e
            heapq.heappush(q,(d+e,i))
m=0
for i,j,e in t:
    s=min(r[i],r[j])
    d=abs(r[i]-r[j])
    m=max(m,s+(e+d)/2)
print(math.floor(m+0.5))