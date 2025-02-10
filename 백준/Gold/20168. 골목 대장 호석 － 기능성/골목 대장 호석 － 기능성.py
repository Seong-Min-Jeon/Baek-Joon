import sys
import heapq
I=sys.stdin.readline
n,m,s,d,c=map(int,I().split())
l=[[] for _ in range(n+1)]
for _ in range(m):
    x,y,z=map(int,I().split())
    l[x].append((y,z))
    l[y].append((x,z))
r=[1e9 for _ in range(n+1)]
q=[(0,0,s)]
while q:
    m,t,p=heapq.heappop(q)
    for y,z in l[p]:
        if(t+z<=c and r[y]>max(m,z)):
            r[y]=max(m,z)
            heapq.heappush(q,(max(m,z),t+z,y))
if(r[d]==1e9): print(-1)
else: print(r[d])