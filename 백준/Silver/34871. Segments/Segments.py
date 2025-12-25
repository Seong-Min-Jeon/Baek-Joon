import sys
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,q=F()
a,b,c,d=1e99,1e99,0,0
for _ in range(n):
    x,y,z=F()
    a=min(a,x)
    b=min(b,y)
    c=max(c,x)
    d=max(d,y)
for _ in range(q):
    p=int(I())
    if(a<=p<=b and c<=p<=d): print(0)
    elif(b<=p<=c): print(max(p-b,c-p))
    elif(p<=b): print(c-p)
    elif(c<=p): print(p-b)