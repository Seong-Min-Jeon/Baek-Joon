M=1000
def f(m,s):    
    if(s==1): return m
    p=f(m,s//2)
    q=g(p,p)
    if(s%2==1): return g(q,m)
    else: return q
def g(a,b):
    r=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                r[i][j]=(r[i][j]+a[i][k]*b[k][j])%M
    return r
n,b=map(int,input().split())
v=[[*map(int,input().split())] for _ in range(n)]
for i in range(n):
    for j in range(n):
        v[i][j]=0 if v[i][j]==1000 else v[i][j]
r=f(v,b)
for e in r:
    print(*e)