def f(x):
    if(len(m)==b):
        s.add(tuple(m))
        return
    for e in l:
        if(e>=x and (l.count(e)>m.count(e))):
            m.append(e)
            f(e)
            m.pop()

a,b=map(int,input().split())
l=sorted(list(map(int,input().split())))
m=[]
s=set()
f(l[0])
for e in sorted(list(s)):
    print(*e)