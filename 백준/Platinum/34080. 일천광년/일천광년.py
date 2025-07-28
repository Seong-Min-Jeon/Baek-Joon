import sys,math
I=sys.stdin.readline
for _ in range(int(I())):
    n,x,y=map(int,I().split())
    g=math.gcd(x,y)
    if(n%(x//g+y//g)==0):
        print(1)
        print((n//(x//g+y//g))*(y//g),x+y)
    else:
        m=n//(x+y)
        z=n-m*(x+y)
        a,b,c,d=0,1,x,y
        d-=x*(z-1)
        c+=x*(z-1)
        b=z
        a=z-1
        t=c//(x+y)
        a-=t
        b-=t
        c-=t*(x+y)
        d+=t*(x+y)
        print(2)
        print(y*m+a,c)
        print(y*m+b,d)