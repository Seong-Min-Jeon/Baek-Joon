def dfs(x,y,c,d):
    if(c>1): print(1); exit()
    if(d==3): return    
    for i,j in ((1,0),(-1,0),(0,1),(0,-1)):
        if(0<=i+x<5 and 0<=j+y<5 and l[x+i][y+j]!=-1 and v[i+x][j+y]==0):
            v[i+x][j+y]=1
            dfs(i+x,j+y,c+l[x+i][y+j],d+1)
            v[i+x][j+y]=0
l=[list(map(int,input().split())) for _ in range(5)]
x,y=map(int,input().split())
v=[[0]*5 for _ in range(5)]
v[x][y]=1
dfs(x,y,0,0)
print(0)