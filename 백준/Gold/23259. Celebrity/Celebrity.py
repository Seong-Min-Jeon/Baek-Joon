import sys
from itertools import permutations as P
I=sys.stdin.readline
x,y=set(),set()
for _ in range(int(I())):
    e=int(I())
    s=set()
    for _ in range(e):
        a,b=map(int,I().split())
        s.add((a-1,b-1))
    r=tuple()
    for p in P((0,1,2,3,4)):
        t=[]        
        for a,b in s:
            c,d=p[a],p[b]
            t.append((min(c,d),max(c,d)))
        t.sort()
        t=tuple(t)
        if(r): r=min(r,t)
        else: r=t
    f=1
    if(r in x): x.remove(r)
    if(r not in y): x.add(r)
    y.add(r)
print(len(x))