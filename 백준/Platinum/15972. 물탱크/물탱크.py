import sys
import heapq
import copy
I=sys.stdin.readline
n,m,h=map(int,I().split())
l=[[h]*m for _ in range(n)]
q=[]
for i in range(n+1):
    for j,p in enumerate(map(int,I().split())):
        if(p<0): continue
        heapq.heappush(q,(p,i-1,j,i,j))
for i in range(n):
    for j,p in enumerate(map(int,I().split())):
        if(p<0): continue
        heapq.heappush(q,(p,i,j-1,i,j))
t=[]
r=[]
while q or t:
    if(not q):
        if(r==l): break
        r=copy.deepcopy(l)
        for x,y1,y2,z1,z2 in t: 
            heapq.heappush(q,(x,y1,y2,z1,z2))
        t.clear()
    p,a1,a2,b1,b2=heapq.heappop(q)
    f=1
    if(a1<0 or a2<0): 
        if(l[b1][b2]>p):
            l[b1][b2]=p; f=0
        else: continue
    if(b1>=n or b2>=m):
        if(l[a1][a2]>p):
            l[a1][a2]=p; f=0
        else: continue
    if(f):
        if(p<l[a1][a2] and p<l[b1][b2]):
            v=min(l[a1][a2],l[b1][b2])
            l[a1][a2],l[b1][b2]=v,v
        if(p<l[a1][a2] and p>=l[b1][b2]):
            l[a1][a2]=p
        if(p>=l[a1][a2] and p<l[b1][b2]):
            l[b1][b2]=p
        t.append((p,a1,a2,b1,b2))
        continue
    for x,y1,y2,z1,z2 in t: 
        heapq.heappush(q,(x,y1,y2,z1,z2))
    t.clear()
print(sum(sum(e) for e in l))