from math import gcd
from math import comb
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

input()
r={}
for e in map(int,input().split()):
    t=[]
    factor(e,t)
    for e in t:
        r[e]=r.get(e,0)+1
c,x=0,0
for k in r:
    if(r[k]>x):
        c,x=1,r[k]
    elif(r[k]==x): c+=1

v=0
for i in range(1,c+1):
    v+=comb(c,i)
print(x)
print(v)