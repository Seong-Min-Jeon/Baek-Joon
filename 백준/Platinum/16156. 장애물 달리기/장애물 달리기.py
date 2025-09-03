import sys,heapq
I=sys.stdin.readline
f=lambda:map(int,I().split())
n,m=f()
l=[list(f()) for _ in range(n)]
if(m==1):
    for _ in range(n):
        print(1)
    exit()
r=[[[(1e99,-1)]*m for _ in range(n)] for _ in range(2)]
q=[]
for i,e in enumerate(l):
    q.append((l[i][m-1],i,m-1,i))
while q:
    d,i,j,s=heapq.heappop(q)
    if(r[0][i][j][0]<d): continue
    for x,y in ((1,0),(-1,0),(0,1),(0,-1)):
        if(0<=i+x<n and 0<=j+y<m and r[0][i+x][j+y][0]>d+l[i+x][j+y]):
            r[0][i+x][j+y]=(d+l[i+x][j+y],s)
            heapq.heappush(q,(d+l[i+x][j+y],i+x,j+y,s))
        if(0<=i+x<n and 0<=j+y<m and r[1][i+x][j+y][0]>d):
            r[1][i+x][j+y]=(d,s)
w=[0]*n
for i in range(n):    
    w[r[1][i][0][1]]+=1
for e in w:
    print(e)