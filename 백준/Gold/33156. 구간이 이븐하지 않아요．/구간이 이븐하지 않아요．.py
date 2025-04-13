def f(a,x):
    for e in a: x[e]=x.get(e,0)+1
    return x
def g(n,x):
    if(x[n]==1): del x[n]
    else: x[n]-=1
    return x
def h(n,x):
    x[n]=x.get(n,0)+1
    return x
n=int(input())
l=list(map(int,input().split()))
for k in range(n-(n%2),0,-2):
    x,y={},{}
    for i in range(n-k+1):
        if(i==0): 
            t=l[i:k+i].copy()
            a,b=t[:k//2],t[k//2:]
            x=f(a,x); y=f(b,y)
        else:
            x=g(l[i-1],x)
            y=g(l[i-1+k//2],y)
            x=h(l[i-1+k//2],x)
            y=h(l[i-1+k],y)
        if(x==y):
            print(k); exit()
print(0)