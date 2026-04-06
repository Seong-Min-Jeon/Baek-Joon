import sys
I=sys.stdin.readline
n,m=map(int,I().split())
a=[*map(int,I().split())]
u,d=[0],[0]
p,q=1e99,0
for e in a:
    if(p>e): u.append(u[-1]+1)
    else: u.append(u[-1])
    if(q<e): d.append(d[-1]+1)
    else: d.append(d[-1])
    p,q=e,e
u.append(u[-1])
d.append(d[-1])
for _ in range(m):
    x,y=map(int,I().split())
    t=0
    if(x>1 and a[x-2]>a[y-1]): t+=1
    if(y<n and a[y]<a[x-1]): t+=1
    if(x>1): t-=1
    print(u[x-1]+d[y]-d[x]+1+u[n]-u[y+1]+t)