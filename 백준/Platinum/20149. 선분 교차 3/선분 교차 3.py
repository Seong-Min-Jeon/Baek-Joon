def f(a,b,x,y,n,m): return (a*y+x*m+n*b)-(a*m+x*b+n*y)
def g():
    t=((a-w)*(x-z)-(b-x)*(w-y))/((a-c)*(x-z)-(b-d)*(w-y))
    p,q=a+t*(c-a),b+t*(d-b)
    if(p==int(p)): p=int(p)
    if(q==int(q)): q=int(q)
    return p,q
a,b,c,d=map(int,input().split())
w,x,y,z=map(int,input().split())
p,q,r,s=f(a,b,c,d,w,x),f(a,b,c,d,y,z),f(w,x,y,z,a,b),f(w,x,y,z,c,d)
if(p*q<0 and r*s<0): print(1); print(*g())
elif((p*q<0 and r*s==0) or (p*q==0 and r*s<0)): print(1); print(*g())
elif(p*q==r*s==0):
    if(p==q==r==s==0):
        if(abs(a-c)+abs(b-d)+abs(w-y)+abs(x-z)==max(a,c,w,y)-min(a,c,w,y)+max(b,d,x,z)-min(b,d,x,z)):
            if(a==w and b==x): print(1); print(a,b)
            elif(a==y and b==z): print(1); print(a,b)
            elif(c==w and d==x): print(1); print(c,d)
            elif(c==y and d==z): print(1); print(c,d)
            else: print(1); print(*g())
        elif((min(a,c)<=w<=max(a,c) and min(b,d)<=x<=max(b,d)) or
            (min(a,c)<=y<=max(a,c) and min(b,d)<=z<=max(b,d)) or
            (min(w,y)<=a<=max(w,y) and min(x,z)<=b<=max(x,z)) or
            (min(w,y)<=c<=max(w,y) and min(x,z)<=d<=max(x,z))): print(1)
        else: print(0)
    else:
        if(a==w and b==x): print(1); print(a,b)
        elif(a==y and b==z): print(1); print(a,b)
        elif(c==w and d==x): print(1); print(c,d)
        elif(c==y and d==z): print(1); print(c,d)
        else: print(0)
else:
    print(0)