def f(x):
    if(len(l)==b):
        print(*l)        
        return
    for i in range(x,a+1):
        l.append(i)
        f(i)
        l.pop()
l=[]
a,b=map(int,input().split())
f(1)