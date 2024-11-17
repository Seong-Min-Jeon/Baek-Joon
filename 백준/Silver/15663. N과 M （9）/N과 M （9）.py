def f():
    if(len(m)==b and tuple(m) not in s):
        print(*m)
        s.add(tuple(m))
        return
    for e in sorted(l):
        if(m.count(e)<l.count(e)):
            m.append(e)
            f()
            m.pop()
a,b=map(int,input().split())
l=list(map(int,input().split()))
s=set()
m=[]
f()