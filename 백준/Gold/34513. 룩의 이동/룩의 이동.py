import sys
from collections import deque as D
I=sys.stdin.readline
n=int(I())
l=[list(I().strip()) for _ in range(n)]
a,b,c,d=0,0,0,0
for i in range(n):
    for j in range(n):
        if(l[i][j]=='R'): a,b=i,j
        if(l[i][j]=='K'): c,d=i,j
r=[[[1e9]*n for _ in range(n)] for _ in range(2)]
r[0][a][b]=1
r[1][a][b]=1
q=D([(0,a,b),(1,a,b)])
while q:
    f,x,y=q.popleft()
    for g,i,j in ((0,1,0),(0,-1,0),(1,0,1),(1,0,-1)):
        if(not (0<=x+i<n and 0<=y+j<n and l[x+i][y+j]!='B')): continue
        if((l[x][y]=='W' or f!=g) and r[g][x+i][y+j]>r[f][x][y]+1):
            r[g][x+i][y+j]=r[f][x][y]+1
            q.append((g,x+i,y+j))
        if(l[x][y]!='W' and f==g and r[f][x+i][y+j]>r[f][x][y]):
            r[f][x+i][y+j]=r[f][x][y]
            q.appendleft((f,x+i,y+j))
t=min(e[c][d] for e in r)
print(t if t!=1e9 else -1)