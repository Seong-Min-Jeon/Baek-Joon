import sys,heapq
I=sys.stdin.readline
F=lambda:map(int,I().split())
n,m=F()
l=[list(F()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if(l[i][j]==-1): l[i][j]=1e99
        elif(l[i][j]==-2): l[i][j]=0
v=1e99
r=[[1e99]*m for _ in range(n)]
q=[]
for s in range(m):
    if(l[0][s]==1e99): continue
    r[0][s]=l[0][s]
    q.append((l[0][s],0,s))
for s in range(n):
    if(l[s][m-1]==1e99): continue
    r[s][m-1]=l[s][m-1]
    q.append((l[s][m-1],s,m-1))
while q:
    d,x,y=heapq.heappop(q)
    if(r[x][y]<d): continue
    for i,j in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
        if(0<=x+i<n and 0<=y+j<m and r[x+i][y+j]>d+l[x+i][y+j]):
            r[x+i][y+j]=d+l[x+i][y+j]
            heapq.heappush(q,(r[x+i][y+j],x+i,y+j))
for i in range(n-1):
    v=min(v,r[i][0])
v=min(v,min(r[-1]))
print(v if v!=1e99 else -1)