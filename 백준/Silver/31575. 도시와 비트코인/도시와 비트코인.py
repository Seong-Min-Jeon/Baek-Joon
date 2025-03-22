n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(m)]
v=[[0]*n for _ in range(m)]
q=[(0,0)]
while q:
    x,y=q.pop()
    if(x==m-1 and y==n-1): print('Yes'); exit()
    if(x+1<m and l[x+1][y]==1 and v[x+1][y]==0): q.append((x+1,y)); v[x+1][y]=1
    if(y+1<n and l[x][y+1]==1 and v[x][y+1]==0): q.append((x,y+1)); v[x][y+1]=1
print('No')