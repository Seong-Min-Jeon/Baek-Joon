import sys
from collections import deque as D
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,m=F()
a,b,c,d=F()
a-=1;b-=1;c-=1;d-=1
l=[list(I().strip()) for _ in range(n)]
r=[[1e9]*m for _ in range(n)]
r[a][b]=0
q=D([(a,b)])
while q:
    x,y=q.popleft()
    for i,j in ((1,0),(-1,0),(0,1),(0,-1)):
        if(0<=x+i<n and 0<=y+j<m):
            if(l[x+i][y+j]=='0' and r[x+i][y+j]>r[x][y]):
                r[x+i][y+j]=r[x][y]
                q.appendleft((x+i,y+j))
            elif(l[x+i][y+j]!='0' and r[x+i][y+j]>r[x][y]+1):
                r[x+i][y+j]=r[x][y]+1
                q.append((x+i,y+j))
print(r[c][d])