def f(m,s):
    if(s==1): return m
    p=f(m,s//2)
    q=g(p,p)
    if(s%2==1): return g(q,m)
    else: return q
def g(a,b):
    r=[[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                r[i][j]=(r[i][j]+a[i][k]*b[k][j])%M
    return r
M=10000
while True:
    n=int(input())
    if(n<0): break
    m=[[1,1],[1,0]]
    print(f(m,n)[0][1] if n!=0 else 0)