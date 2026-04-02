import sys
sys.setrecursionlimit(10**6)
I=sys.stdin.readline
F=lambda:map(int,I().split())
def f(i,j):
    if(i==m-1 and j==n-1): return 1
    if(d[i][j]>=0): return d[i][j]
    d[i][j]=0
    for x,y in ((1,0),(-1,0),(0,1),(0,-1)):
        if(0<=i+x<m and 0<=j+y<n and l[i+x][j+y]<l[i][j]):
            d[i][j]+=f(i+x,j+y)
    return d[i][j]
m,n=F()
l=[[*F()] for _ in range(m)]
d=[[-1]*n for _ in range(m)]
print(f(0,0))