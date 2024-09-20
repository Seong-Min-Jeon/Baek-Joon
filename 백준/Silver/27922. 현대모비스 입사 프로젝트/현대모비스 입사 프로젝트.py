import sys
ip=sys.stdin.readline
a,b=map(int,ip().split())
p,q,r=[],[],[]
for _ in range(a):
    l,m,n=map(int,ip().split())
    p.append(l+m)
    q.append(l+n)
    r.append(m+n)
p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)
x,y,z=0,0,0
for i in range(b):
    x+=p[i]
    y+=q[i]
    z+=r[i]
print(max(x,y,z))