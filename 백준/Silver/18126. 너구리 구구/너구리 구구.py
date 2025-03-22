import heapq
import sys
I=sys.stdin.readline
n=int(input())
l=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c=map(int,I().split())
    l[a].append((c,b))
    l[b].append((c,a))
r=[0]*(n+1)
v=[0]*(n+1)
q=[(0,1)]
v[1]=1
while q:
    d,p=heapq.heappop(q)
    d*=-1
    if(r[p]>d): continue
    for c,b in l[p]:
        if(r[b]<d+c and v[b]==0):
            heapq.heappush(q,(-(d+c),b))
            r[b]=d+c
            v[b]=1
print(max(r))