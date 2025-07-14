import sys
I=sys.stdin.readline
for _ in range(int(I())):
    t={}
    for _ in range(int(I())-1):
        a,b=map(int,I().split())
        t[b]=a
    x,y=map(int,I().split())
    p,q=[x],[y]
    while True:
        if(p[-1] not in t): break
        p.append(t[p[-1]])
    while True:
        if(q[-1] not in t): break
        q.append(t[q[-1]])
    q=set(q)
    for e in p:
        if(e in q): print(e); break