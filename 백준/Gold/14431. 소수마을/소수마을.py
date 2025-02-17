import sys
import heapq
I=sys.stdin.readline
a,b,x,y=map(int,I().split())
d=set([i for i in range(2,5000)])
for i in range(2,5001):
    for j in range(2*i,5001,i):
        if(j in d): d.remove(j)
n=int(I())
l=[tuple(map(int,I().split())) + (i+1,) for i in range(n)]
l.append((x,y,n+1))
r=[1e9 for _ in range(n+2)]
q=[(0,a,b,0)]
while q:
    k,i,j,p=heapq.heappop(q)
    if(k>r[p]): continue
    for f,g,h, in l:
        t=int(((i-f)**2+(j-g)**2)**0.5)
        if(t in d and r[h]>t+k): 
            r[h]=t+k
            heapq.heappush(q,(t+k,f,g,h))
if(r[-1]==1e9): print(-1)
else: print(r[-1])