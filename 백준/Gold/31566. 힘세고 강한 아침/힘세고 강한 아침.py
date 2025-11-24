import sys
I=sys.stdin.readline
F=lambda:map(int,I().split())
def f():
    n,m,q=F()
    l=[[[1e99]*n for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        b,t,c=F()
        b-=1;t-=1
        for i,e in enumerate(l):
            if(b!=i and t!=i): e[b][t]=c
    for k in range(n):
        for t in range(n):
            if(t!=k): l[t][k][k]=0
        for i in range(n):
            for j in range(n):
                for t in range(n):
                    l[t][i][j]=min(l[t][i][j],l[t][i][k]+l[t][k][j])
    for _ in range(q):
        s,k,e=F()
        s-=1;k-=1;e-=1
        print(l[k][s][e] if l[k][s][e]!=1e99 else 'No')
f()