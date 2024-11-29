def f(x):
    if(len(m)==b):
        if(tuple(m) not in s):
            print(*m)
            s.add(tuple(m))
        return
    for e in l:
        if(e>=x):
            m.append(e)
            f(e)
            m.pop()

a,b=map(int,input().split())
l=sorted(list(map(int,input().split())))
s=set()
m=[]
f(l[0])