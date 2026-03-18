P=998244353
G=3

def ntt(a,inv=0):
    n=len(a); j=0
    for i in range(1,n):
        b=n>>1
        while j&b: j^=b; b>>=1
        j^=b
        if i<j: a[i],a[j]=a[j],a[i]
    l=2
    while l<=n:
        w=pow(G,(P-1)//l,P)
        if(inv): w=pow(w,P-2,P)
        for i in range(0,n,l):
            x=1
            for j in range(i,i+l//2):
                u,v=a[j],a[j+l//2]*x%P
                a[j]=(u+v)%P
                a[j+l//2]=(u-v)%P
                x=x*w%P
        l*=2
    if(inv):
        x=pow(n,P-2,P)
        for i in range(n): a[i]=a[i]*x%P

def conv(a,b):
    la,lb=len(a),len(b)
    n=1
    need=la+lb-1
    while n<need:n<<=1
    fa=a+[0]*(n-la)
    fb=b+[0]*(n-lb)
    ntt(fa); ntt(fb)
    c=[fa[i]*fb[i]%P for i in range(n)]
    ntt(c,1)
    c=c[:need]    
    return c if c else [0]

n,m=map(int,input().split())
a,b=list(input().strip()),list(input().strip())
r=[]
for p,q in (('S','R'),('P','S'),('R','P')):
    x,y=[],[]
    for i in range(n):
        if(a[i]==p): x.append(1)
        else: x.append(0)
    for i in range(m):
        if(b[i]==q): y.append(1)
        else: y.append(0)
    r.append(conv(x,y[::-1]))
z=0
for i in range(n+m-1):
    if(i<m-1): continue
    z=max(z,sum([r[j][i] for j in range(3)]))
print(z)