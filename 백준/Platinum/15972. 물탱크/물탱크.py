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
        heapq.heappush(q,(p,(i-1,j),(i,j)))
for i in range(n):
    for j,p in enumerate(map(int,I().split())):
        if(p<0): continue
        heapq.heappush(q,(p,(i,j-1),(i,j)))
t=[]
r=[]
while q or t:
    if(not q):
        if(r==l): break
        r=copy.deepcopy(l)
        for x,y,z in t: heapq.heappush(q,(x,y,z)); t.clear()
    p,a,b=heapq.heappop(q)
    f=1
    if(a[0]<0 or a[1]<0): 
        if(l[b[0]][b[1]]>p):
            l[b[0]][b[1]]=p; f=0
        else: continue
    if(b[0]>=n or b[1]>=m):
        if(l[a[0]][a[1]]>p):
            l[a[0]][a[1]]=p; f=0
        else: continue
    if(f):
        if(p<l[a[0]][a[1]] and p<l[b[0]][b[1]]):
            v=min(l[a[0]][a[1]],l[b[0]][b[1]])
            l[a[0]][a[1]],l[b[0]][b[1]]=v,v
        if(p<l[a[0]][a[1]] and p>=l[b[0]][b[1]]):
            l[a[0]][a[1]]=p
        if(p>=l[a[0]][a[1]] and p<l[b[0]][b[1]]):
            l[b[0]][b[1]]=p
        t.append((p,a,b))
        continue
    for x,y,z in t: 
        heapq.heappush(q,(x,y,z))
    t.clear()
print(sum(sum(e) for e in l))