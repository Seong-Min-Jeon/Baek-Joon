import sys
from collections import deque as D
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,m=F()
l=[list(I().strip()) for _ in range(n)]
d={}
for i,e in enumerate(((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1))):
    d[i]=e
for _ in range(int(I())):
    w,x,y,z=F()
    w-=1; x-=1; y-=1; z-=1
    r=[[1e9]*m for _ in range(n)]
    r[w][x]=0
    q=D([(w,x)])
    while q:
        i,j=q.popleft()
        a,b=d[int(l[i][j])]
        if(0<=i+a<n and 0<=j+b<m and r[i+a][j+b]>r[i][j]):
            r[i+a][j+b]=r[i][j]
            q.appendleft((i+a,j+b))
        for a,b in ((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)):
            if(0<=i+a<n and 0<=j+b<m and r[i+a][j+b]>r[i][j]+1):
                r[i+a][j+b]=r[i][j]+1
                q.append((i+a,j+b))
    print(r[y][z])