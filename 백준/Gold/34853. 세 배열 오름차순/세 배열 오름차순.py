import sys
from bisect import bisect_left as B
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,q=F()
l=[[]]
for _ in range(n):
    _,*t=F()
    l.append(sorted(t))
for _ in range(q):
    a,b,c,j=F()
    x,z=1,10**9
    while x<=z:
        y=(x+z)//2
        if(B(l[a],y)+B(l[b],y)+B(l[c],y)<j): x=y+1
        else: z=y-1
    print(z)