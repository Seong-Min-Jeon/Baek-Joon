import sys
I=sys.stdin.readline
n,m=map(int,I().split())
l=[[1e9 for _ in range(n)] for _ in range(n)]
r=[[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,z=map(int,I().split())
    x-=1; y-=1
    l[x][y]=min(l[x][y],z)
    l[y][x]=min(l[y][x],z)
    r[x][y]=y+1
    r[y][x]=x+1
for k in range(n):
    l[k][k]=0
    for i in range(n):
        for j in range(n):
            if(l[i][j]>l[i][k]+l[k][j]):
                l[i][j]=l[i][k]+l[k][j]
                r[i][j]=r[i][k]
for k in range(n):
    r[k][k]='-'
    print(*r[k])