def f(v,p,q):
    if(v==0): return 1
    a,b=0,0
    if(v//p in r): a=r[v//p]
    else: a=f(v//p,p,q); r[v//p]=a
    if(v//q in r): b=r[v//q]
    else: b=f(v//q,p,q); r[v//q]=b
    return a+b
n,p,q=map(int,input().split())
r={}
print(f(n,p,q))