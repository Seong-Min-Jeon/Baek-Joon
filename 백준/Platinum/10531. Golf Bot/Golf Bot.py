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

# 두 수의 convolution
# a,b는 int 배열 [1, 2, 3]
def conv(a,b):
    n=1
    while n<len(a)+len(b)-1: n<<=1
    a=a+[0]*(n-len(a)); b=b+[0]*(n-len(b))
    ntt(a); ntt(b)
    c=[a[i]*b[i]%P for i in range(n)]
    ntt(c,1)
    return c[:len(a)+len(b)-n-1]

import sys
I=sys.stdin.readline
a=[0]*200001
for _ in range(int(I())):
    a[int(I())]=1
c=conv(a,a)
s=set()
for i,e in enumerate(a):
    if(e): s.add(i)
for i,e in enumerate(c):
    if(e): s.add(i)
r=0
for _ in range(int(I())):
    if(int(input()) in s):
        r+=1
print(r)