import sys
I=sys.stdin.readline
n,m=map(int,I().split())
l=[[1e9]*(n+1) for _ in range(n+1)]
t=set()
for _ in range(m):
    x,y,z=map(int,I().split())
    l[x][y]=min(l[x][y],z)
    l[y][x]=min(l[y][x],z)
    t.add((x,y,z))
for k in range(n+1):
    l[k][k]=0
    for i in range(n+1):
        for j in range(n+1):
            l[i][j]=min(l[i][j],l[i][k]+l[k][j])
r=1e9
for k in range(n+1):
    m=0
    for i,j,e in t:
        s=min(l[k][i],l[k][j])
        d=abs(l[k][i]-l[k][j])
        m=max(m,s+(e+d)/2)
    r=min(r,m)
print(r)