import sys
from collections import defaultdict as D
I=sys.stdin.readline
n,m=map(int,I().split())
l=[tuple(map(int,I().split())) for _ in range(n)]
d=D(list)
for _ in range(m):
    a,b=map(int,I().split())
    d[a].append(b)
    d[b].append(a)
s=set([i+1 for i in range(n)])
r=1e99
while s:
    t=[s.pop()]
    q=[t[0]]
    while q:
        p=q.pop()
        for e in d[p]:
            if(e not in s): continue
            q.append(e)
            t.append(e)
            s.remove(e)
    c=[l[e-1] for e in t]
    c.sort()
    a=c[0][0]
    x=c[-1][0]
    c.sort(key=lambda x:x[1])
    b=c[0][-1]
    y=c[-1][-1]
    r=min(r,2*(x-a+y-b))
print(r)