import sys
from collections import deque as d
I=sys.stdin.readline
n,m=map(int,I().split())
h,p,s,z=(),[],[],set()
for i in range(n):
    t=I().strip()
    for j in range(m):
        if(t[j]=='H'): h=(i,j)
        elif(t[j]=='P'): p.append((i,j))
        elif(t[j]=='#'): s.append([i,j,0])
        elif(t[j]=='X'): z.add((i,j))
v=[[-1]*m for _ in range(n)]
v[h[0]][h[1]]=0
q=d([h])
while q:
    x,y=q.popleft()
    for a,b in ((1,0),(0,1),(-1,0),(0,-1)):
        if(0<=x+a<n and 0<=y+b<m and ((x+a),(y+b)) not in z and v[x+a][y+b]<0):
            v[x+a][y+b]=v[x][y]+1
            q.append(((x+a),(y+b)))
for i,j in p:
    w=[[-1]*m for _ in range(n)]
    w[i][j]=0
    q=d([(i,j)])
    while q:
        x,y=q.popleft()
        for a,b in ((1,0),(0,1),(-1,0),(0,-1)):
            if(0<=x+a<n and 0<=y+b<m and ((x+a),(y+b)) not in z and w[x+a][y+b]<0):
                w[x+a][y+b]=w[x][y]+1
                q.append(((x+a),(y+b)))
    for i in range(len(s)):
        a,b,c=s[i]
        if(w[a][b]<=v[a][b] and v[a][b]>=0 and w[a][b]>=0): s[i][2]+=1
s.sort(key=lambda k: k[2])
print(s[-1][2])