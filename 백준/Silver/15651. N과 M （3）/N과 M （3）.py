def f():
    if(len(l)==b):
        print(*l)
        return
    for i in range(1,a+1):
        l.append(i)
        f()
        l.pop()

a,b=map(int,input().split())
l=[]
f()