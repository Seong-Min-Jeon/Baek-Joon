import sys
from math import gcd
ip=sys.stdin.readline

n,b=map(int,input().split())
x,y=0,0
for _ in range(n):
    t=ip().split()
    x,y=x+int(t[0]),y+int(t[1])
if(x==0): print('EZPZ'); exit()
p=y-n*b
if(p%x==0): print(p//x); exit()
t=gcd(p,x)
r1,r2=p//t,x//t
if(r2<0): print(f'{-r1}/{-r2}')
else: print(f'{r1}/{r2}')