import sys
I=sys.stdin.readline
F=lambda:map(int,I().split())
for _ in range(int(I())):
    n,m,k=F()
    l=[[] for _ in range(n+1)]
    for _ in range(m):
        a,b=F()
        l[a].append(b)
        l[b].append(a)
    t=[*F()]
    v=set(t)
    for e in t:
        for p in l[e]:
            v.add(p)
    print(len(v))