import sys
ip=sys.stdin.readline
n,m,b=map(int,ip().split())
g=[list(map(int,ip().split())) for _ in range(n)]
t,h=10**9,0
for e in range(257):
    x,y=0,b
    for i in range(n):
        for j in range(m):
            if(g[i][j]<e): y-=e-g[i][j]; x+=e-g[i][j]
            elif(g[i][j]>e): y+=g[i][j]-e; x+=2*(g[i][j]-e)
    if(y<0): break
    if(t>x or (t==x and h<e)): t,h=x,e
print(t,h)