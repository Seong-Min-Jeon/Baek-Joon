import sys
I=sys.stdin.readline
n,q=map(int,I().split())
l=[[[1e9]*(n+1) for _ in range(n+1)] for _ in range(n+1)]
for i in range(n):
    for j,e in enumerate(map(int,I().split())):
        if(e!=0): l[i+1][j+1][0]=e
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            l[i][j][k]=min(l[i][j][k-1],l[i][k][k-1]+l[k][j][k-1])
for _ in range(q):
    c,s,e=map(int,I().split())
    if(s==e): print(0); continue
    print(-1 if l[s][e][c-1]==1e9 else l[s][e][c-1])