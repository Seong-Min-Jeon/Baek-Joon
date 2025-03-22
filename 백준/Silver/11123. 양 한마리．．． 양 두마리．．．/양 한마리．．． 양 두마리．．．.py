import sys
I=sys.stdin.readline
for _ in range(int(I())):
    n,m=map(int,I().split())
    l=[list(I().strip()) for _ in range(n)]
    v=[[0]*m for _ in range(n)]
    c=0
    for i in range(n):
        for j in range(m):
            if(v[i][j]==1 or l[i][j]=='.'): continue
            q=[(i,j)]
            while q:
                x,y=q.pop(0)
                for a,b in ((1,0),(-1,0),(0,-1),(0,1)):
                    if(0<=x+a<n and 0<=y+b<m and v[x+a][y+b]==0 and l[x+a][y+b]=='#'):
                        q.append((x+a,y+b))
                        v[x+a][y+b]=1
            c+=1
    print(c)