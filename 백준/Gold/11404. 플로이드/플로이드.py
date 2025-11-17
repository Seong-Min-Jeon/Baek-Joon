import sys
I=sys.stdin.readline
n,m=int(I()),int(I())
l=[[1e99]*n for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,I().split())
    a-=1; b-=1
    l[a][b]=min(l[a][b],c)
for k in range(n):
    l[k][k]=0
    for i in range(n):
        for j in range(n):
            l[i][j]=min(l[i][j],l[i][k]+l[k][j])
for i in range(n):
    for j in range(n):
        if(l[i][j]==1e99): l[i][j]=0
for i in range(n):
    print(*l[i])