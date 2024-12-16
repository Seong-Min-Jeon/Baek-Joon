import sys
ip=sys.stdin.readline
a=int(ip())
r,g,b=map(int,ip().split())
for _ in range(a-1):
    x,y,z=map(int,ip().split())
    x+=min(g,b)
    y+=min(r,b)
    z+=min(r,g)
    r,g,b=x,y,z
print(min(r,g,b))
