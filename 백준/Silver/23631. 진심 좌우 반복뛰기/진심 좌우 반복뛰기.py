import sys
I=sys.stdin.readline
for _ in range(int(I())):
    n,k=map(int,I().split())
    x,z=0,n-1
    while x<=z:
        y=(x+z)//2
        if(n-1<(k*y*(y+1))//2): z=y-1
        else: x=y+1
    t=(k*z*(z+1))//2
    if(z%2==0):
        print(-(k*z//2)+n-t-1,'R')
    else:
        print(k*(z+1)//2-(n-t)+1,'L')