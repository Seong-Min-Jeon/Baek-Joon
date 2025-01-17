def f(x,y,r,c):
    global a
    if(x==1): return
    x//=2
    y//=2
    if(r>=x and c>=y): a+=3*x*y; f(x,y,r-x,c-y)
    elif(r<x and c>=y): a+=x*y; f(x,y,r,c-y)
    elif(r>=x and c<y): a+=2*x*y; f(x,y,r-x,c)
    else: f(x,y,r,c)

n,r,c=map(int,input().split())
a=0
x,y=2**n,2**n
f(x,y,r,c)
print(a)