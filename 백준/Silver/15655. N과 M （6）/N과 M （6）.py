def f(x):    
    if(len(m)==b):
        print(*m)
        return
    for e in l:
        if(x<e):
            m.append(e)
            f(e)
            m.pop()

a,b=map(int,input().split())
l=sorted(list(map(int,input().split())))
m=[]
f(0)