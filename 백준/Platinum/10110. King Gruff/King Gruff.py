import sys,heapq
from bisect import bisect_right as B
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,m,a,b=F()
l=[]
u=[[] for _ in range(n+1)]
w=[[] for _ in range(n+1)]
for _ in range(m):
    x,y,d,c=F()
    l.append([x,y,d,c])
    u[x].append((y,d))
    w[y].append((x,d))
r=[[1e99]*(n+1) for _ in range(2)]
r[0][a]=0
q=[(0,a)]
while q:
    d,p=heapq.heappop(q)
    if(r[0][p]<d): continue
    for i,e in u[p]:
        if(r[0][i]>d+e):
            r[0][i]=d+e
            heapq.heappush(q,(d+e,i))
r[1][b]=0
q=[(0,b)]
while q:
    d,p=heapq.heappop(q)
    if(r[1][p]<d): continue
    for i,e in w[p]:
        if(r[1][i]>d+e):
            r[1][i]=d+e
            heapq.heappush(q,(d+e,i))
t=[]
for i in range(m):
    x,y,d,c=l[i]
    t.append((r[0][x]+d+r[1][y],c))
t.sort()
v=[0]
for d,c in t:
    v.append(v[-1]+c)
d=[x for x,_ in t]
for _ in range(int(I())):
    print(v[B(d,int(I()))])