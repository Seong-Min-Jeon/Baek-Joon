from collections import deque
import copy
import sys
I=sys.stdin.readline
m,n=map(int,I().split())
l=[list(map(int,I().split())) for _ in range(n)]
q=deque([])
for i in range(n):
    for j in range(m):
        if(l[i][j]==1):
            q.append((i,j))
c=-1
d=[(-1,0),(1,0),(0,-1),(0,1)]
p=deque([])
while q:
    i,j=map(int,q.popleft())
    for x,y in d:
        x+=i
        y+=j
        if(x>=0 and x<n and y>=0 and y<m and l[x][y]==0):
            l[x][y]=1; p.append((x,y))
    if(len(q)==0): q=copy.deepcopy(p); p.clear(); c+=1
r=c
for i in range(n):
    for j in range(m):
        if(l[i][j]==0):
            r=-1
print(r)