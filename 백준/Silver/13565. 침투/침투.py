import sys
sys.setrecursionlimit(10**6)
def f(x,y):
    global m,r
    if(not (0<=x<m and 0<=y<n)): return
    if(l[x][y]==1 or v[x][y]==1): return
    if(x==m-1): r=1; return
    v[x][y]=1
    f(x+1,y); f(x-1,y); f(x,y+1); f(x,y-1)
m,n=map(int,input().split())
l=[list(map(int,list(input().strip()))) for _ in range(m)]
v=[[0]*n for _ in range(m)]
r=0
for i in range(n): f(0,i)
if(r): print('YES')
else: print('NO')