def f():
    if(len(m)==b):
        print(*m)
        return
    for e in l:
        if(e not in m):
            m.append(e)
            f()
            m.pop()

a,b=map(int,input().split())
l=sorted(list(map(int,input().split())))
m=[]
f()