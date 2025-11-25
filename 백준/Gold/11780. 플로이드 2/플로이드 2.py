import sys
I=sys.stdin.readline
def f(a,b):
    if r[a][b]<0: return []
    p=[a]
    while a!=b:
        a=r[a][b]
        p.append(a)
    return p
n,m=int(I()),int(I())
l=[[1e99]*n for _ in range(n)]
r=[[-1]*n for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,I().split())
    a-=1;b-=1
    if(l[a][b]>c):
        l[a][b]=c
        r[a][b]=b
for k in range(n):
    l[k][k]=0
    for i in range(n):
        for j in range(n):
            if(l[i][j]>l[i][k]+l[k][j]):
                l[i][j]=l[i][k]+l[k][j]
                r[i][j]=r[i][k]
for i in range(n):
    for j in range(n):
        if(l[i][j]==1e99):
            l[i][j]=0
for e in l:
    print(*e)
for i in range(n):
    for j in range(n):
        t=f(i,j)
        if(len(t)==1): print(0)
        else: print(len(t),end=' '); print(*[i+1 for i in t])