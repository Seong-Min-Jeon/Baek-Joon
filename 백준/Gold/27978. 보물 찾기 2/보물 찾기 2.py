import sys
from collections import deque as D
I=sys.stdin.readline
n,m=map(int,I().split())
l=[list(I().strip()) for _ in range(n)]
a,b,u,w=0,0,0,0
for i in range(n):
    for j in range(m):
        if(l[i][j]=='K'): a,b=i,j
        if(l[i][j]=='*'): u,w=i,j
r=[[1e9]*m for _ in range(n)]
r[a][b]=0
q=D([(a,b)])
while q:
    i,j=q.popleft()
    for x,y in ((1,0),(1,1),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)):
        if(0<=x+i<n and 0<=y+j<m and l[x+i][y+j]!='#'):
            if(y==1 and r[x+i][y+j]>r[i][j]):
                r[x+i][y+j]=r[i][j]
                q.appendleft((x+i,y+j))
            if(y!=1 and r[x+i][y+j]>r[i][j]+1):
                r[x+i][y+j]=r[i][j]+1
                q.append((x+i,y+j))
print(r[u][w] if r[u][w]!=1e9 else -1)