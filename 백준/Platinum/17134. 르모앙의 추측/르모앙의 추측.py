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
    n=1
    while n<len(a)+len(b)-1: n<<=1
    a=a+[0]*(n-len(a)); b=b+[0]*(n-len(b))
    ntt(a); ntt(b)
    c=[a[i]*b[i]%P for i in range(n)]
    ntt(c,1)
    return c[:len(a)+len(b)-n-1]

p=[1]*(10**6)
p[0],p[1]=0,0
for i in range(2,10**6):
    if(p[i]==1):
        for j in range(2*i,10**6,i):
            p[j]=0

m=[0]*(10**6)
for i in range(5*10**5):
    if(p[i]==1): m[2*i]=1

a,b=[0]*5*10**5,[0]*5*10**5
for i in range(10**6):
    if(p[i]==1): a[i//2]=1
for i in range(10**6):
    if(m[i]==1): b[i//2]=1

c=conv(a,b)

import sys
I=sys.stdin.readline
for _ in range(int(I())):
    print(c[int(I())//2])