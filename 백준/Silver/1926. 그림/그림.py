import sys
I=sys.stdin.readline
n,m=map(int,I().split())
l=[list(map(int,I().split())) for _ in range(n)]
v=[[0]*m for _ in range(n)]
c,r=0,0
for i in range(n):
    for j in range(m):
        if(v[i][j]==1 or l[i][j]==0): continue
        z=0
        q=[(i,j)]
        while q:
            x,y=q.pop(0)
            z+=1
            for a,b in ((1,0),(-1,0),(0,-1),(0,1)):
                if(0<=x+a<n and 0<=y+b<m and v[x+a][y+b]==0 and l[x+a][y+b]==1):
                    q.append((x+a,y+b))
                    v[x+a][y+b]=1
        c+=1
        r=max(r,z)
print(c)
if(r<=1): print(r)
else: print(r-1)