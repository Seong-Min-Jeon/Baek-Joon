import sys
from bisect import bisect_left as b
I=sys.stdin.readline
n,m=map(int,I().split())
l=[]
d={}
for _ in range(n):
    x,y=I().split()
    y=int(y)
    l.append(y)
    if(y not in d): d[y]=x
for _ in range(m):
    v=int(I())
    print(d[l[b(l,v)]])