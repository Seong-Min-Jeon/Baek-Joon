import sys
I=sys.stdin.readline
n,m=map(int,I().split())
l=[int(I()) for _ in range(n)]
s=set(l)
l.sort()
for _ in range(m):
    d=int(I())
    if(d not in s): print(-1); continue
    x,z=0,n-1
    while x<=z:
        y=(x+z)//2        
        if(l[y]<d): x=y+1
        else: z=y-1
    print(x)