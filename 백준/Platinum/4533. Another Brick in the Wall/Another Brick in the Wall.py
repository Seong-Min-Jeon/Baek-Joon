import sys
from collections import deque as D
I=sys.stdin.readline
for _ in range(int(I())):
    n,m=map(int,I().split())
    l=[list(I().strip()) for _ in range(n)]
    r=[[1e99]*m for _ in range(n)]
    r[0]=[1]*m
    q=D([(1,0,i) for i in range(m)])
    while q:
        d,i,j=q.popleft()
        if(r[i][j]<d): continue
        for x,y in ((1,0),(-1,0),(0,1),(0,-1)):
            if(0<=x+i<n and 0<=y+j<m):
                if(l[i][j]!=l[x+i][y+j] and r[x+i][y+j]>d+1):
                    r[x+i][y+j]=d+1
                    q.append((d+1,x+i,y+j))
                if(l[i][j]==l[x+i][y+j] and r[x+i][y+j]>d):
                    r[x+i][y+j]=d
                    q.appendleft((d,x+i,y+j))    
    print(min(r[-1]))