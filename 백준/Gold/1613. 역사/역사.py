import sys
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,k=F()
l=[[1e99]*n for _ in range(n)]
for _ in range(k):
    a,b=F()
    a-=1; b-=1
    l[a][b]=1
for k in range(n):
    l[k][k]=0
    for i in range(n):
        for j in range(n):
            l[i][j]=min(l[i][j],l[i][k]+l[k][j])
m=int(I())
for _ in range(m):
    a,b=F()
    a-=1; b-=1
    if(l[a][b]==l[b][a]): print(0)
    else: print(-1 if l[a][b]!=1e99 else 1)