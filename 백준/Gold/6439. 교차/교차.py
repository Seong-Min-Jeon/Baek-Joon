import sys
I=sys.stdin.readline
def f(a,b,x,y,n,m): return (a*y+x*m+n*b)-(a*m+x*b+n*y)
def h(a,b,c,d,x,y):
    return min(a,c)<=x<=max(a,c) and min(b,d)<=y<=max(b,d)
def g(p,q):
    a,b,c,d=p
    w,x,y,z=q
    if(f(a,b,c,d,w,x)*f(a,b,c,d,y,z)<0 and f(w,x,y,z,a,b)*f(w,x,y,z,c,d)<0): return True
    if(f(a,b,c,d,w,x)==0 and f(a,b,c,d,y,z)==0 and f(w,x,y,z,a,b)==0 and f(w,x,y,z,c,d)==0 and
       (h(a,b,c,d,w,x) or h(a,b,c,d,y,z) or h(w,x,y,z,a,b) or h(w,x,y,z,c,d))):
        return True
    if(f(a,b,c,d,w,x)==0 and h(a,b,c,d,w,x)): return True
    if(f(a,b,c,d,y,z)==0 and h(a,b,c,d,y,z)): return True
    if(f(w,x,y,z,a,b)==0 and h(w,x,y,z,a,b)): return True
    if(f(w,x,y,z,c,d)==0 and h(w,x,y,z,c,d)): return True
    return False
for _ in range(int(I())):
    a,b,c,d,w,x,y,z=map(int,I().split())
    p=(a,b,c,d)
    w,x,y,z=min(w,y),min(x,z),max(w,y),max(x,z)
    if(g(p,(w,x,w,z)) or g(p,(w,x,y,x)) or g(p,(y,z,y,x)) or g(p,(y,z,w,z))):
        print('T')
    elif(w<a<y and w<c<y and x<b<z and x<d<z):
        print('T')
    else:
        print('F')