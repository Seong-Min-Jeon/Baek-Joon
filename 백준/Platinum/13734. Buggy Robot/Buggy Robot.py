import sys
from collections import deque as D
I=sys.stdin.readline
n,m=map(int,I().split())
l=[list(I().strip()) for _ in range(n)]
h=I().strip()
s,g=0,0
for i in range(n):
    for j in range(m):
        if(l[i][j]=='S'): s=(i,j)
        elif(l[i][j]=='G'): g=(i,j)
r=[[[1e9]*m for _ in range(n)] for _ in range(len(h)+1)]
r[0][s[0]][s[1]]=0
q=D([(0,0,s[0],s[1])])
while q:
    c,d,x,y=q.popleft()
    if(r[d][x][y]<c): continue
    for i,j in ((1,0),(-1,0),(0,1),(0,-1)):
        v=0
        if(d<len(h) and h[d]=='D' and (i,j)==(1,0)): v=1
        elif(d<len(h) and h[d]=='R' and (i,j)==(0,1)): v=1
        elif(d<len(h) and h[d]=='L' and (i,j)==(0,-1)): v=1
        elif(d<len(h) and h[d]=='U' and (i,j)==(-1,0)): v=1
        if(v):
            if(0<=x+i<n and 0<=y+j<m and l[x+i][y+j]!='#' and r[d+1][x+i][y+j]>c):
                r[d+1][x+i][y+j]=c
                q.appendleft((c,d+1,x+i,y+j))
            if(0>x+i or x+i>=n or 0>y+j or y+j>=m or l[x+i][y+j]=='#'):
                q.appendleft((c,d+1,x,y))
        if(0<=x+i<n and 0<=y+j<m and l[x+i][y+j]!='#' and r[d][x+i][y+j]>c+1):
            r[d][x+i][y+j]=c+1
            q.append((c+1,d,x+i,y+j))
    if(d<len(h) and r[d+1][x][y]>c+1):
        r[d+1][x][y]=c+1
        q.append((c+1,d+1,x,y))
print(min([r[i][g[0]][g[1]] for i in range(len(h)+1)]))