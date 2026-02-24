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

def g(r,a):
    global x
    if(a in x): return
    x.add(a)
    t=r.copy()
    for e in r:
        t.remove(e)
        g(t,a*e)

def f(n):
    global x
    x.clear()
    if(n==0): return 1
    r=[]
    factor(n,r)
    g(r,1)
    s=0
    for e in x:
        if(e%4): s+=e
    return 8*s

x=set()

n=int(input())
s=f(n)
print(s)

for i in range(1,10**10):
    if(n<i**2): break
    s+=2*f(n-i**2)
print(s)