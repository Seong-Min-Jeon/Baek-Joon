from math import gcd
from random import randrange

def is_prime(n):
    if(n<2): return 0
    A=(2,3,5,7,11,13,17,19,23,29,31,37)
    for p in A:
        if(n%p==0): return n==p
    d,s=n-1,0
    while d%2==0:
        d//=2
        s+=1
    for a in A:
        x=pow(a,d,n)
        if(x==1) or (x==n-1): continue
        for _ in range(s-1):
            x=x*x%n
            if(x==n-1): break
        else:
            return 0
    return 1

def rho(n):
    if(n%2==0): return 2
    while 1:
        x=y=randrange(2, n - 1)
        c=randrange(1, n - 1)
        d=1
        while d==1:
            x=(x*x+c)%n
            y=(y*y+c)%n
            y=(y*y+c)%n
            d=gcd(abs(x-y),n)
        if(d!=n): return d

def factor(n,r):
    if(n==1): return
    if(is_prime(n)): r.append(n); return
    d=rho(n)
    factor(d,r)
    factor(n//d,r)

def compress(r):
    r.sort()
    c=[]
    for p in r:
        if(c and c[-1][0]==p):
            c[-1][1]+=1
        else:
            c.append([p,1])
    return c

def div(c,i,a):
    if(i==len(c)):
        x.append(a); return
    p,e=c[i]
    t=1
    for _ in range(e+1):
        div(c,i+1,a*t)
        t*=p

import sys
I=sys.stdin.readline
while True:
    n=int(I())
    if(n==0): break
    l=len(str(n))
    if(l%2): print(f'{n}: no'); continue
    r=[]
    factor(n,r)
    c=compress(r)

    x=[]
    div(c,0,1)
    v=[]
    for e in x:
        if(l//2==len(str(e))):
            v.append(e)

    f=0
    for i in v:
        for j in v:
            if(n==i*j and sorted(str(n))==sorted(str(i)+str(j))
               and '00' not in str(i) and '00' not in str(j)):
                f=1
            if(f): break
    print(f'{n}: yes' if f else f'{n}: no')