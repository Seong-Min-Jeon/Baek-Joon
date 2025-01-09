import sys
ip=sys.stdin.readline
n,m=map(int,ip().split())
l=[list(map(int,ip().strip())) for _ in range(n)]
v=[[0 for _ in range(m)] for _ in range(n)]
q=[(0,0)]
v[0][0]=1
while q:
    x,y=q[0][0],q[0][1]
    q.pop(0)
    if(0<x and v[x-1][y]==0 and l[x-1][y]==1): q.append((x-1,y)); v[x-1][y]=v[x][y]+1
    if(x<n-1 and v[x+1][y]==0 and l[x+1][y]==1): q.append((x+1,y)); v[x+1][y]=v[x][y]+1
    if(0<y and v[x][y-1]==0 and l[x][y-1]==1): q.append((x,y-1)); v[x][y-1]=v[x][y]+1
    if(y<m-1 and v[x][y+1]==0 and l[x][y+1]==1): q.append((x,y+1)); v[x][y+1]=v[x][y]+1
print(v[n-1][m-1])