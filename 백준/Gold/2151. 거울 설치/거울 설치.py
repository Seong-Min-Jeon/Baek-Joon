import sys,heapq
I=sys.stdin.readline
n=int(I())
l=[list(I().strip()) for _ in range(n)]
a,b,c,d=-1,-1,-1,-1
for i in range(n):
    for j in range(n):
        if(l[i][j]=='#' and a<0): a,b=i,j
        elif(l[i][j]=='#'): c,d=i,j
r=[[[1e99]*n for _ in range(n)] for _ in range(2)]
r[0][a][b]=0
r[1][a][b]=0
q=[(0,0,a,b),(0,1,a,b)]
while q:
    v,w,x,y=heapq.heappop(q)
    if(r[w][x][y]<v): continue
    for i,j in ((1,0),(-1,0),(0,1),(0,-1)):
        if(i==0 and w): continue
        if(j==0 and not w): continue
        if(0<=x+i<n and 0<=y+j<n and l[x+i][y+j]=='!' and r[abs(w-1)][x+i][y+j]>v+1):
            r[abs(w-1)][x+i][y+j]=v+1
            heapq.heappush(q,(v+1,abs(w-1),x+i,y+j))
        if(0<=x+i<n and 0<=y+j<n and l[x+i][y+j]!='*' and r[w][x+i][y+j]>v):
            r[w][x+i][y+j]=v
            heapq.heappush(q,(v,w,x+i,y+j))
print(min(r[0][c][d],r[1][c][d]))