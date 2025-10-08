import sys
from collections import deque as D
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,m,k=F()
l=[list(F()) for _ in range(n)]
a,c=0,10**10
while a<=c:
    b=(a+c)//2
    r=[[1e9]*m for _ in range(n)]
    r[0][0]=0
    q=D([(0,0)])
    while q:
        x,y=q.popleft()
        for i,j in ((1,0),(-1,0),(0,1),(0,-1)):
            if(0<=x+i<n and 0<=y+j<m):
                if(l[x+i][y+j]>b and r[x+i][y+j]>r[x][y]+1):
                    r[x+i][y+j]=r[x][y]+1
                    q.append((x+i,y+j))
                if(l[x+i][y+j]<=b and r[x+i][y+j]>r[x][y]):
                    r[x+i][y+j]=r[x][y]
                    q.appendleft((x+i,y+j))
    if(r[-1][-1]<=k): c=b-1
    else: a=b+1
print(a)