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
M=100
x,y,a,b,r=map(int,input().split())
m=[[b*x+a*y,b],[b,a]]
k=[[x,1],[y,0]]
z=''
if(r==0): z=str(x)
elif(r==1): z=str(y)
elif(r==2): z=str(m[0][0])
elif(r>2): z=str(g(m,f(k,r-2))[0][0])
if(len(z)==1): print('0'+z)
else: print(z)