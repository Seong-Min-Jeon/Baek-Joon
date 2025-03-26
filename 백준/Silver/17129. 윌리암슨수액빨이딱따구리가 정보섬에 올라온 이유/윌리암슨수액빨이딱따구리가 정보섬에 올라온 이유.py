from collections import deque as dq
import sys
I=sys.stdin.readline
n,m=map(int,I().split())
l=[list(map(int,list(I().strip()))) for _ in range(n)]
a,b=0,0
r=[]
for i in range(n):
    for j in range(m):
        if(l[i][j]==2): a,b=i,j
        elif(l[i][j]>2): r.append((i,j))
v=[[-1]*m for _ in range(n)]
q=dq([(a,b,0)])
while q:
    i,j,d=q.popleft()
    for x,y in ((1,0),(-1,0),(0,1),(0,-1)):
        if(0<=i+x<n and 0<=j+y<m and v[i+x][j+y]==-1 and l[i+x][j+y]!=1):
            v[i+x][j+y]=d+1
            q.append((i+x,j+y,d+1))
m=10**9
for i,j in r:
    if(v[i][j]!=-1): m=min(m,v[i][j])
if(m==10**9): print('NIE')
else: print('TAK'); print(m)