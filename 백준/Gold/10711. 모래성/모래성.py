import sys
from collections import deque as D
I=sys.stdin.readline
h,w=map(int,I().split())
l=[list(I().strip()) for _ in range(h)]
d=((1,0),(0,1),(1,1),(0,-1),(1,-1),(-1,0),(-1,1),(-1,-1))
v=[[-1]*w for _ in range(h)]
c=[[0]*w for _ in range(h)]
q=D([])
for i in range(h):
    for j in range(w):
        if(l[i][j]!='.'):
            t=0
            for x,y in d:
                if(l[i+x][j+y]=='.'): t+=1
            c[i][j]=t
            if(t>=int(l[i][j])):
                v[i][j]=1
                q.append((i,j))
        else: v[i][j]=0
while q:
    i,j=q.popleft()
    for x,y in d:
        if(v[i+x][j+y]>=0): continue
        c[i+x][j+y]+=1
        if(c[i+x][j+y]>=int(l[i+x][j+y])):
            v[i+x][j+y]=v[i][j]+1
            q.append((i+x,j+y))
print(max([max(e) for e in v]))