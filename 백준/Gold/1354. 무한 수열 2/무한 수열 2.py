def f(n,p,q,x,y):
    if(n<=0): return 1
    if(n//p-x not in d): d[n//p-x]=f(n//p-x,p,q,x,y)
    if(n//q-y not in d): d[n//q-y]=f(n//q-y,p,q,x,y)
    a,b=d[n//p-x],d[n//q-y]
    return a+b

n,p,q,x,y=map(int,input().split())
d={}
print(f(n,p,q,x,y))