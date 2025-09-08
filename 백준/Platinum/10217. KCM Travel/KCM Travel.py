import sys
from collections import deque as D
def F():
    I=sys.stdin.readline
    for _ in range(int(I())):
        n,m,k=map(int,I().split())
        l=[[] for _ in range(n+1)]
        for _ in range(k):
            u,v,c,d=map(int,I().split())
            l[u].append((d,c,v))
        for i in range(n+1):
            l[i].sort()
        r=[[1e99]*(m+1) for _ in range(n+1)]
        r[1][0]=0
        q=D([(0,0,1)])
        while q:
            x,y,p=q.popleft()
            if(r[p][y]<x): continue
            for d,c,i in l[p]:
                if(c+y<=m and r[i][c+y]>d+x):
                    for t in range(c+y,m+1):
                        if(d+x<r[i][t]): r[i][t]=d+x
                        else: break
                    q.append((d+x,c+y,i))
        t=min(r[n])
        print(t if t!=1e99 else "Poor KCM")
F()