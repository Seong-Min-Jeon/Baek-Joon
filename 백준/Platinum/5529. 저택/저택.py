import sys,heapq
from collections import defaultdict as D
I=sys.stdin.readline
m,n,z=map(int,I().split())
a,b=D(list),D(list)
f=0
for _ in range(z):
    i,j=map(int,I().split())
    a[i].append(j)
    b[j].append(i)
    if((i,j)==(1,1)): f=1
a[m].append(n)
b[n].append(m)
a[1].append(1)
b[1].append(1)
u,w=D(list),D(list)
for k in a.keys():
    a[k].sort()
    for i in range(len(a[k])-1):
        u[(k,a[k][i])].append((k,a[k][i+1],a[k][i+1]-a[k][i]))
        u[(k,a[k][i+1])].append((k,a[k][i],a[k][i+1]-a[k][i]))
for k in b.keys():
    b[k].sort()
    for i in range(len(b[k])-1):
        w[(b[k][i],k)].append((b[k][i+1],k,b[k][i+1]-b[k][i]))
        w[(b[k][i+1],k)].append((b[k][i],k,b[k][i+1]-b[k][i]))
r=D(lambda:1e99)
q=[(0,1,1,0)]
while q:
    d,i,j,t=heapq.heappop(q)
    if(t):
        for x,y,v in w[(i,j)]:
            if(r[(x,y)]>d+v):
                r[(x,y)]=d+v
                heapq.heappush(q,(d+v,x,y,t))
                if((x,y)==(1,1)):
                    if(f): heapq.heappush(q,(d+v+1,x,y,abs(t-1)))
                else: heapq.heappush(q,(d+v+1,x,y,abs(t-1)))                
    else:
        for x,y,v in u[(i,j)]:
            if(r[(x,y)]>d+v):
                r[(x,y)]=d+v
                heapq.heappush(q,(d+v,x,y,t))
                if((x,y)==(1,1)):
                    if(f): heapq.heappush(q,(d+v+1,x,y,abs(t-1)))
                else: heapq.heappush(q,(d+v+1,x,y,abs(t-1)))
print(r[(m,n)] if r[(m,n)]!=1e99 else -1)