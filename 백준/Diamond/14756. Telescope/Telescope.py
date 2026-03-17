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

import sys
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,l,m,w=F()
t=[[*F()] for _ in range(m)]
p=[[*F()] for _ in range(m)]
r=[]
for i in range(m):
    r.append(conv(t[i],p[i][::-1]))
x=0
for i in range(n+l-1):
    if(i<l-1 or i>=n): continue
    s=0
    for j in range(m):
        s+=r[j][i]
    if(s>w): x+=1
print(x)