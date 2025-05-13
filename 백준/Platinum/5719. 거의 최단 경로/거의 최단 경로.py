import heapq
from collections import deque as dq
import sys
I=sys.stdin.readline
while True:
    n,m=map(int,I().split())
    if(n==m==0): break
    s,d=map(int,I().split())
    l={}
    for _ in range(m):
        u,v,p=map(int,I().split())
        if(u in l): l[u].append((v,p))
        else: l[u]=[(v,p)]
    v=[1e9 for _ in range(n)]
    r=[[] for _ in range(n)]
    q=[(0,s)]
    v[s]=0
    while q:
        c,p=heapq.heappop(q)
        if(v[p]<c): continue
        if(p not in l): continue
        for x,y in l[p]:
            if(v[x]>c+y):
                v[x]=c+y
                r[x]=[p]
                heapq.heappush(q,(c+y,x))
            elif(v[x]==c+y):
                r[x].append(p)
    t={}
    q=dq([d])
    v=[0 for _ in range(n)]
    while q:
        p=q.popleft()
        if(v[p]==0):
            v[p]=1
            for e in r[p]:
                if(e in t): t[e].append(p)
                else: t[e]=[p]
                q.append(e)
    v=[1e9 for _ in range(n)]
    q=[(0,s)]
    v[s]=0
    while q:
        c,p=heapq.heappop(q)
        if(v[p]<c): continue
        if(p not in l): continue
        for x,y in l[p]:
            if(p in t and x in t[p]): continue
            if(v[x]>c+y):
                v[x]=c+y
                heapq.heappush(q,(c+y,x))
    if(v[d]==1e9): print(-1)
    else: print(v[d])