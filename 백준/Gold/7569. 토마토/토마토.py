from collections import deque
import copy
import sys
I=sys.stdin.readline
m,n,h=map(int,I().split())
l=[]
for _ in range(h):
    t=[]
    for _ in range(n):
        t.append(list(map(int,I().split())))
    l.append(t)
q=deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if(l[i][j][k]==1):
                q.append((i,j,k))
c=-1
p=deque([])
while q:
    i,j,k=map(int,q.popleft())    
    if(i>0 and l[i-1][j][k]==0): l[i-1][j][k]=1; p.append((i-1,j,k))
    if(i<h-1 and l[i+1][j][k]==0): l[i+1][j][k]=1; p.append((i+1,j,k))
    if(j>0 and l[i][j-1][k]==0): l[i][j-1][k]=1; p.append((i,j-1,k))
    if(j<n-1 and l[i][j+1][k]==0): l[i][j+1][k]=1; p.append((i,j+1,k))
    if(k>0 and l[i][j][k-1]==0): l[i][j][k-1]=1; p.append((i,j,k-1))
    if(k<m-1 and l[i][j][k+1]==0): l[i][j][k+1]=1; p.append((i,j,k+1))
    if(len(q)==0): q=copy.deepcopy(p); p.clear(); c+=1
r=c
for i in range(h):
    for j in range(n):
        for k in range(m):
            if(l[i][j][k]==0):
                r=-1
print(r)