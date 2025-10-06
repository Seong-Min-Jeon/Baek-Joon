import sys
from collections import deque as D
I=sys.stdin.readline
def f(a,b,c,d,e):
    if(0<=a<n and 0<=b<m and 0<=c<n+1 and 0<=d<m+1):
        if(l[a][b]==e):
            if(r[c][d]>r[x][y]):
                r[c][d]=r[x][y]
                q.appendleft((c,d))
        else:
            if(r[c][d]>r[x][y]+1):
                r[c][d]=r[x][y]+1
                q.append((c,d))
n,m=map(int,I().split())
l=[list(I().strip()) for _ in range(n)]
r=[[1e9]*(m+1) for _ in range(n+1)]
r[0][0]=0
q=D([(0,0)])
while q:
    x,y=q.popleft()
    f(x-1,y-1,x-1,y-1,'\\')
    f(x-1,y,x-1,y+1,'/')
    f(x,y-1,x+1,y-1,'/')
    f(x,y,x+1,y+1,'\\')
print(r[-1][-1] if r[-1][-1]!=1e9 else 'NO SOLUTION')