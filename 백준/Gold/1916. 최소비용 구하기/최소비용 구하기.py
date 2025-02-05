import sys
import heapq
I=sys.stdin.readline
n,m=int(I()),int(I())
f=1e8
l=[[f for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,I().split())
    l[a-1][b-1]=min(l[a-1][b-1],c)
r=[f for _ in range(n)]
x,y=map(int,I().split())
q=[(0,x-1)]
r[x-1]=0
while q:
    d,p=heapq.heappop(q)
    if(r[p]<d): continue
    for i,e in enumerate(l[p]):
        if(d+e<r[i]):
            r[i]=d+e
            heapq.heappush(q,(d+e,i))
print(r[y-1])