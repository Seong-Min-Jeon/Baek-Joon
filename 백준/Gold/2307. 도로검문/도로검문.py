import heapq
import sys

def f(l,f,a,b):
    r=[1e9]*(n+1)
    r[1]=0
    p=[0]*(n+1)
    q=[(0,1)]
    while q:
        d,x=heapq.heappop(q)
        if(r[x]<d): continue
        for y,z in l[x]:
            if((x==a and y==b) or (x==b and y==a)): continue
            if(r[y]>d+z):
                heapq.heappush(q,(d+z,y))
                r[y]=d+z
                p[y]=x
    if(f): return r[-1]
    else:
        p[0]=r[-1] 
        return p

I=sys.stdin.readline
n,m=map(int,I().split())
l=[[] for _ in range(n+1)]
for _ in range(m):
    x,y,z=map(int,I().split())
    l[x].append((y,z))
    l[y].append((x,z))
p=f(l,0,0,0)
t=[]
x=n
while x!=1:
    t.append((x,p[x]))
    x=p[x]
r=0
for a,b in t:
    r=max(r,f(l,1,a,b))
if(r==1e9): print(-1)
else: print(r-p[0])